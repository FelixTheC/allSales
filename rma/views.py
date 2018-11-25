from django.shortcuts import render, redirect
from django.utils.timezone import now
from datetime import datetime
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.views.generic import CreateView

from prioListe.utils import searching
from .forms import RefursbishmentForm
from .forms import RefursbishmentUpdateForm
from .forms import RMASearchForm
from .models import Refurbisment
import os


def handle_uploaded_files(f, filepath, filename):
    try:
        with open('media/' + filepath + filename, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except FileNotFoundError:
        os.mkdir('media/' + filepath)
        handle_uploaded_files(f, filepath, filename)


def get_files(request, file_liste, clear=''):
    clear = request.POST.get('rma_file-clear')
    salesPerson = request.POST.get('salesPerson')
    for file in request.FILES.getlist('rma_file'):
        try:
            handle_uploaded_files(file, 'media/' + salesPerson + '/', str(file))
        except:
            pass
        file_liste.append(str(file))


class RefurbishmentFormView(CreateView):
    form_class = RefursbishmentForm
    template_name = 'rma_form.html'
    file_liste = []

    def get_success_url(self):
        return reverse('rma:home')

    def form_valid(self, form):
        return super(RefurbishmentFormView, self).form_valid(form)


class RefurbishmentUpdateView(UpdateView):
    model = Refurbisment
    form_class = RefursbishmentUpdateForm
    template_name = 'rma_form.html'
    file_liste = []
    clear = None

    def get_success_url(self):
        return reverse('rma:home')
    
    def form_valid(self, form):
        return super(RefurbishmentUpdateView, self).form_valid(form)

    def get_initial(self):
        initial = super(RefurbishmentUpdateView, self).get_initial()
        if str(self.object.parcel_received) == '2000-01-01':
            initial['parcel_received'] = now()
        else:
            initial['parcel_received'] = self.object.parcel_received
        return initial


def refurbishment_list(request):
    object_list = Refurbisment.objects.all().exclude(status__name='Out in Production for Refurbishment')
    return rma_main_list(request, object_list)


def search_customer(request):
    if request.method == 'POST':
        form = RMASearchForm(request.POST)
        if form.is_valid():
            search_string = form['search'].value()
            if search_string == '':
                return redirect(reverse('rma:home'))
            else:
                t = searching(Refurbisment, search_string)
                liste = Refurbisment.objects.none()
                for i in t:
                    liste = i | liste  # merge Querysets

            return rma_main_list(request, liste)
        else:
            return redirect(reverse('rma:home'))
    else:
        return redirect(reverse('rma:home'))


def rma_main_list(request, object_list):
    context = {
        'object_list': object_list,
        'search_form': RMASearchForm,
    }
    return render(request, template_name='rma_list.html', context=context)


class RMADelete(DeleteView):
    model = Refurbisment
    template_name = 'rma_notice_delete.html'
    success_url = reverse_lazy('rma:home')

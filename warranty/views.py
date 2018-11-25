from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from prioListe.utils import searching
from .forms import WarrantyForm
from .forms import WarrantyUpdateForm
from .models import Warranty


class WarrantyFormView(CreateView):
    form_class = WarrantyForm
    template_name = 'w_form.html'

    def get_success_url(self):
        return reverse('warranty:home')

    def form_valid(self, form):
        return super(WarrantyFormView, self).form_valid(form)


class WarrantyUpdateView(UpdateView):
    model = Warranty
    form_class = WarrantyUpdateForm
    template_name = 'w_form.html'

    def get_success_url(self):
        return reverse('warranty:home')

    def form_valid(self, form):
        return super(WarrantyUpdateView, self).form_valid(form)


class WarrantyList(ListView):
    model = Warranty
    template_name = 'w_list.html'
    queryset = Warranty.objects.filter(deleted=False)

    def get_context_data(self, **kwargs):
        return super(WarrantyList, self).get_context_data(**kwargs)


def search_customer(request):
    if request.method == 'POST':
        search_string = request.POST.get('searchfield')
        t = searching(Warranty, search_string)
        customer_list = Warranty.objects.none()
        for i in t:
            customer_list = i | customer_list  # merge Querysets
        context = {
            'object_list': customer_list.filter(deleted=False)
        }
    return render(request, 'w_list.html', context=context)


class WarrantyDelete(DeleteView):
    model = Warranty
    template_name = 'w_notice_delete.html'
    success_url = reverse_lazy('warranty:home')
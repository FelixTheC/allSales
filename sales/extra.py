from datetime import date
from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import DetailView, DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from faktura.models import Contacts
from ordercontact.models import Ordercontactinvoiceaddresse as OrdercontactOrdercontactinvoiceaddresse
from survey.models import SalesSalesinputsurvey
from prioListe.models import PriolisteAssignment
from collar.models import Animalspecies
from prioListe.forms import CreateFormFromOrder


class CollarDetailView(DetailView):
    referer = ''

    def __init__(self, model, template_name):
        super(CollarDetailView, self).__init__()
        self.model = model
        self.template_name = template_name

    def get_context_data(self, **kwargs):
        context = super(CollarDetailView, self).get_context_data(**kwargs)
        try:
            context['inPrioListe'] = PriolisteAssignment.objects.filter(ordering_number=self.object.operation_Number)
        except AttributeError:
            context['inPrioListe'] = PriolisteAssignment.objects.filter(ordering_number=self.object.operation_number)
        try:
            context['collar_num_list'] = [self.object.number_of_collars.split('$'),
                                        self.object.battery_size.split('$'),
                                        self.object.nom_collar_circumference.split('$')]
        except AttributeError:
            pass
        try:
            contacts = Contacts.objects.get(id_contact=self.object.contacts_faktura_id)
            invoice_addr = OrdercontactOrdercontactinvoiceaddresse.objects.get(pk=self.object.customer_invoice_addresse.pk)
            if invoice_addr.organisation_name in contacts.faktura_address \
                    or invoice_addr.organisation_name in contacts.organisation:
                context['add_exists'] = True
        except:
            context['add_exists'] = False
        return context


class CollarUpdateAllFieldsView(UpdateView):
    form_class = ''
    input_model = None

    def __init__(self, model, input_model, template_name, form_class):
        super(CollarUpdateAllFieldsView, self).__init__()
        self.model = model
        self.input_model = input_model
        self.template_name = template_name
        self.form_class = form_class

    def get_context_data(self, **kwargs):
        salesInput = self.input_model.objects.filter(order=self.object.pk).order_by('pk')

        context = super(CollarUpdateAllFieldsView, self).get_context_data(**kwargs)
        context['type'] = self.object.get_model_type
        try:
            context['operationNumber'] = self.object.operation_Number
        except AttributeError:
            context['operationNumber'] = self.object.operation_number
        context['animals'] = Animalspecies.objects.all().order_by('name')
        context['pk'] = self.object.pk
        try:
            context['max_num'] = len(self.object.number_of_collars.split('$')[:-1])
        except AttributeError:
            context['max_num'] = 0
        context['count_prod_rec'] = len(salesInput)
        context['airtime_contract'] = self.object.airtime_contract
        context['prodRec'] = salesInput
        context['pos1_dist'] = ['', '1', '1.5', '3']
        context['range_twenty'] = [i for i in range(1, 21)]
        context['punching2'] = ['__', 'M4/7mm', 'M5/8mm']
        context['gl_no'] = [i for i in range(4)]
        context['gl_fixes'] = [i for i in range(3)]
        context['ir_fixes'] = [i for i in range(19)]
        return context

    def form_valid(self, form):
        return super(CollarUpdateAllFieldsView, self).form_valid(form)

    def get_success_url(self):
        return reverse('sales:listsorders')


class CreateProductionRecord(CreateView):
    model = None
    order_model = None
    form_class = None
    template_name = ''

    def __init__(self, model, order_model, form_class, template_name):
        self.model = model
        self.order_model = order_model
        self.form_class = form_class
        self.template_name = template_name

    def get_success_url(self):
        return reverse('sales:listsorders')

    def get_context_data(self, **kwargs):
        context = super(CreateProductionRecord, self).get_context_data(**kwargs)
        context['animals'] = Animalspecies.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        order_obj = self.order_model.objects.get(pk=kwargs['pk'])
        input_form = self.form_class(request.POST)
        form_fields = self.model.__dict__['__doc__'].split('(')[1].split(',')
        if input_form.is_valid():
            salesinput = self.model()
            for i in form_fields[:-1]:
                if i != 'id':
                    try:
                        i = i.strip().replace('(', '')
                    except AttributeError:
                        pass
                    else:
                        try:
                            if 'pos' in i or 'neg' in i:
                                salesinput.__dict__[i] = int(input_form[i].value())
                            else:
                                salesinput.__dict__[i] = input_form[i].value()
                        except KeyError:
                            if 'no_of' in i or 'fixes' in i:
                                salesinput.__dict__[i] = 0
                            else:
                                salesinput.__dict__[i] = ''
                        except AttributeError:
                            pass
            salesinput.order = order_obj
            salesinput.save()
            return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = "/";</script>')
        else:
            return super(CreateProductionRecord, self).form_invalid(input_form)


class ProductionRecordInitial(CreateView):
    model = None
    order_model = None
    form_class = None
    template_name = ''

    def __init__(self, model, order_model, form_class, template):
        self.model = model
        self.order_model = order_model
        self.form_class = form_class
        self.template_name = template

    def get_success_url(self):
        return reverse('sales:listsorders')

    def post(self, request, *args, **kwargs):
        order_obj = self.order_model.objects.get(pk=kwargs['pk'])
        input_form = self.form_class(request.POST)
        if input_form.is_valid():
            form = input_form.save()
            new_salesinput = self.model.objects.get(pk=form.pk)
            new_salesinput.order = order_obj
            new_salesinput.save()
            return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = "/";</script>')
        else:
            return super(ProductionRecordInitial, self).form_invalid(input_form)


class ProductionRecordUpdate(UpdateView):
    model = None
    form_class = None
    order_model = None
    template_name = ''

    def __init__(self, model, order_model, form_class, template):
        self.model = model
        self.order_model = order_model
        self.form_class = form_class
        self.template_name = template

    def get_context_data(self, **kwargs):
        context = super(ProductionRecordUpdate, self).get_context_data(**kwargs)
        context['object'] = self.order_model.objects.get(pk=kwargs['pk'])

    def get_success_url(self):
        return reverse('sales:listsorders')

    def form_valid(self, form):
        return super(ProductionRecordUpdate, self).form_valid(form)


class ModelDelete(DeleteView):
    model = None
    template_name = 'confirm_delete.html'

    def __init__(self, model):
        self.model = model

    def get_context_data(self, **kwargs):
        context = super(ModelDelete, self).get_context_data(**kwargs)
        context['obj'] = kwargs['object']
        return context

    def post(self, request, *args, **kwargs):
        return reverse('sales:listsorders')

    def get_success_url(self, **kwargs):
        obj = self.model.objects.get(pk=kwargs['pk'])
        if obj.order_acceptet:
            return reverse('sales:listdoneorders')
        else:
            return reverse('sales:listsorders')


class CreatePrioEntryByOrder(CreateView):
    model = PriolisteAssignment
    form_class = CreateFormFromOrder
    template_name = 'surveyProdRec.html'
    order_model = None
    order = None
    hardware_string = None

    def __init__(self, order_model, hardware_string):
        self.order_model = order_model
        self.hardware_string = hardware_string

    def get_context_data(self, **kwargs):
        context = super(CreatePrioEntryByOrder, self).get_context_data(**kwargs)
        context['write_into_prioListe'] = True
        return context

    def post(self, request, *args, **kwargs):
        form = CreateFormFromOrder(request.POST)
        self.order = self.order_model.objects.get(pk=kwargs['pk'])
        prod_recs = SalesSalesinputsurvey.objects.filter(order=self.order.pk)
        if form.is_valid():
            self.order.order_acceptet = True
            self.order.save()
            prioAssignment = form.save(commit=False)
            try:
                prioAssignment.staff = self.order.customer_staff + '/' + prod_recs[0].co_worker
            except IndexError:
                prioAssignment.staff = self.order.customer_staff
            except TypeError:
                prioAssignment.staff = self.order.customer_staff
            prioAssignment.time_in_weeks = 12
            prioAssignment.status = 'Vertrieb'
            prioAssignment.customer = self.order.customer_invoice_address.contact_person
            prioAssignment.hardware = self.hardware_string()
            try:
                prioAssignment.ordering_number = self.order.operation_Number
            except AttributeError:
                prioAssignment.ordering_number = self.order.operation_number
            try:
                if self.order.external_dropoff or self.order.internal_dropff:
                    prioAssignment.drop_off = True
            except AttributeError:
                prioAssignment.drop_off = False
            prioAssignment.created_at = date.today()
            prioAssignment.time_in_weeks = 12
            prioAssignment.finished_until = date.today() + timedelta(days=12*7)
            prioAssignment.has_box = False
            prioAssignment.save()
            return redirect(reverse('pListe:update', kwargs={'pk': prioAssignment.pk}))
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super(CreatePrioEntryByOrder, self).form_invalid(form)


def production_record_update(request, pk, inputmodel, urlname):
    salesinput = inputmodel.objects.get(pk=pk)
    if request.method == 'POST':
        form_fields = inputmodel.__dict__['__doc__'].split('(')[1].split(',')
        for i in form_fields[:-1]:
            if i != 'id':
                try:
                    i = i.strip().replace('(', '')
                except AttributeError:
                    pass
                else:
                    try:
                        if 'pos' in i or 'neg' in i:
                            salesinput.__dict__[i] = int(request.POST[i])
                        else:
                            salesinput.__dict__[i] = request.POST[i]
                    except MultiValueDictKeyError:
                        if 'no_of' in i or 'fixes' in i:
                            salesinput.__dict__[i] = 0
                        else:
                            salesinput.__dict__[i] = ''
                    except AttributeError:
                        pass
        salesinput.save()
        return redirect(reverse(f'sales:{urlname}', kwargs={'pk': salesinput.order.pk}))
    else:
        return redirect(reverse(f'sales:{urlname}', kwargs={'pk': salesinput.order.pk}))
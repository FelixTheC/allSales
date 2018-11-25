from string import ascii_letters
from string import digits
from random import choice
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.urls import reverse
from easy_pdf.views import PDFTemplateView
from sales.forms import SearchForm, StaffChoiceForm
from weasyprint import HTML
from allSales import settings
from vertexLite.models import Vertexliteordermodel
from survey.models import SalesSalesinputsurvey
from allSales.settings import BASE_DIR
from staff.models import Staff
from prioListe.models import PriolisteAssignment
from django.core.exceptions import ObjectDoesNotExist
from survey.models import Surveyordermodel
from miniFawn.models import Minifawnordermodel
from trapTransmitter.models import Traptransmitterordermodel
from django import forms
from collar.models import Animalspecies
from collar.models import ContactTypes
from prioListe.utils import searching

ADMINLISTDISPLAY = (
        'operation_number', 'number_of_collars', 'delivery_addresse', 'origin'
    )

ANIMALSPECIES = set()
ANIMALSPECIES.add(('', ''))
for animal in Animalspecies.objects.all():
    ANIMALSPECIES.add((animal.name, animal.name))

COWORKER = set()
COWORKER.add(('', ''))
for staff in Staff.objects.all():
    COWORKER.add((staff.initialies, staff.name))

PUNCHING1 = (
    ('', ''),
    ('1', '1'),
    ('1.5', '1.5'),
    ('3', '3')
)
#collarDB -> beltfastener
PUNCHING2 = (
    ('', ''),
    ('M4', 'M4/7mm'),
    ('M5', 'M5/8mm'),
)
#CollarDb -> contact_types
IRIDIUM_CONTRACT_TYPES = set()
for contact in ContactTypes.objects.all():
    IRIDIUM_CONTRACT_TYPES.add(
        (contact.name, contact.name)
    )

PRODRECWIDGETS = {
            'animal_species': forms.Select(choices=ANIMALSPECIES, attrs={
                'class': 'sales-input',
            }),
            'co_worker': forms.Select(choices=COWORKER, attrs={
                'class': 'sales-input',
            }),
            'punching1_dist': forms.Select(choices=PUNCHING1, attrs={
                'class': 'sales-input',
            }),
            'punching1_pos': forms.NumberInput(attrs={
                'min': '1', 'max': '20', 'step': '1', 'class': 'sales-input',
            }),
            'punching1_neg': forms.NumberInput(attrs={
                'min': '1', 'max': '20', 'step': '1', 'class': 'sales-input',
            }),
            'punching2': forms.Select(choices=PUNCHING2, attrs={
                'class': 'sales-input',
            }),
            'further_instructions_belt': forms.Textarea(attrs={
                'rows': 4, 'cols': 40, 'class': 'sales-instruction',
            }),
            'order': forms.NumberInput(attrs={
                'class': 'hide_me',
            }),
            'gps_schedule_name': forms.TextInput(attrs={
               'class': 'sales-instruction',
            }),
            'vhf_schedule_name': forms.TextInput(attrs={
                'class': 'sales-instruction',
            }),
            'gl_no_of_attempts': forms.NumberInput(attrs={
                'min': '1', 'max': '3', 'step': '1', 'class': 'sales-input',
            }),
            'gl_fixes_per_message': forms.NumberInput(attrs={
                'min': '1', 'max': '2', 'step': '1', 'class': 'sales-input',
            }),
            'ir_contract_type': forms.Select(choices=IRIDIUM_CONTRACT_TYPES, attrs={
                'class': 'sales-input',
            }),
            'ir_fixes_per_message': forms.NumberInput(attrs={
                'min': '1', 'max': '18', 'step': '1', 'class': 'sales-input',
            }),
            'path_customer_folder': forms.TextInput(attrs={
                'class': 'sales-instruction',
            }),
        }

MINIPRODWIDGETS = {
            'punching1_dist': forms.Select(choices=PUNCHING1, attrs={
                'class': 'sales-input',
            }),
            'punching1_pos': forms.NumberInput(attrs={
                'min': '1', 'max': '20', 'step': '1', 'class': 'sales-input',
            }),
            'punching1_neg': forms.NumberInput(attrs={
                'min': '1', 'max': '20', 'step': '1', 'class': 'sales-input',
            }),
            'punching2': forms.Select(choices=PUNCHING2, attrs={
                'class': 'sales-input',
            }),
            'further_instructions_belt': forms.Textarea(attrs={
                'rows': 4, 'cols': 40, 'class': 'sales-instruction',
            }),
        }


def createHash():
    arr = ascii_letters + digits
    hash = ''
    for i in range(0, 12):
        hash += choice(arr)
    return hash


class PDFView(PDFTemplateView):

    template_name = ''
    obj = None
    pdf_filename = ''
    download_filename = ''
    original = False
    prodrec = False

    def __init__(self, obj, template_name, **kwargs):
        super().__init__(**kwargs)
        self.obj = obj
        self.template_name = template_name
        try:
            self.original = kwargs['original']
        except KeyError:
            pass
        try:
            self.original = kwargs['prodrec']
        except KeyError:
            pass

    def dispatch(self, request, *args, **kwargs):
        return super(PDFView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        date = datetime.now().date().strftime('%y%m%d')
        try:
            obj = self.obj.objects.get(pk=kwargs['pk'])
        except KeyError:
            all_obj = self.obj.objects.all()
            obj = all_obj[0]
        try:
            if self.original:
                self.pdf_filename = f'original_{obj.customer_faktura_id}_InputAcknowledgment_{date}.pdf'
                self.download_filename = f'original_{obj.customer_faktura_id}_InputAcknowledgment_{date}.pdf'
            else:
                self.pdf_filename = f'order_{obj.customer_faktura_id}_InputAcknowledgment_{date}.pdf'
                self.download_filename = f'order_{obj.customer_faktura_id}_InputAcknowledgment_{date}.pdf'
        except TypeError:
            self.pdf_filename = 'None.pdf'
            self.download_filename = 'None.pdf'
        return super(PDFView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PDFView, self).get_context_data(pagesize='A4')
        obj = get_object_or_404(self.obj, pk=kwargs['pk'])
        staff_obj = Staff.objects.get(initialies=obj.customer_staff)
        context['space'] = int(26 - (len(obj.vhf_beacon_frequency))/100)
        context['object'] = obj
        context['customer_mail'] = staff_obj.email
        context['customer_name'] = staff_obj.name
        context['base_url'] = 'file://'.join(settings.STATIC_ROOT) + '/'
        return context


class ProdRecView(PDFTemplateView):

    template_name = ''
    obj = None
    pdf_filename = ''
    download_filename = ''
    finished_until = None
    from_prio = False
    test = False
    order_obj = None
    input_obj = None
    minifawn = False

    def __init__(self, obj, template_name, **kwargs):
        super().__init__(**kwargs)
        self.obj = obj
        self.template_name = template_name
        self.from_prio = kwargs['from_prio']
        self.order_obj = kwargs['order_obj']
        self.input_obj = kwargs['input_obj']
        try:
            self.test = kwargs['test']
        except KeyError:
            pass
        try:
            self.minifawn = kwargs['minifawn']
        except KeyError:
            pass

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(ProdRecView, self).dispatch(request, *args, **kwargs)
        except IndexError:
            print('indexerror')
            obj = self.order_obj.objects.get(pk=kwargs['pk'])
            return redirect(obj.get_sells_detail_url())

    def get(self, request, *args, **kwargs):
        date = datetime.today().date().strftime('%y%m%d')
        try:
            obj = self.obj.objects.get(pk=kwargs['pk'])
        except KeyError:
            all_obj = self.obj.objects.all()
            obj = all_obj[0]
        try:
            if self.from_prio:
                self.pdf_filename = f'production_record_{obj.ordering_number}_{date}.pdf'
                self.download_filename = f'production_record_{obj.ordering_number}_{date}.pdf'
            else:
                self.pdf_filename = f'pre_production_record_{obj.customer_faktura_id}_PRoductionRecord_{date}.pdf'
                self.download_filename = f'pre_production_record_{obj.customer_faktura_id}_PRoductionRecord_{date}.pdf'
        except TypeError:
            self.pdf_filename = 'None.pdf'
            self.download_filename = 'None.pdf'
        return super(ProdRecView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProdRecView, self).get_context_data(pagesize='A4')
        progress_number = ''
        if self.from_prio:
            assignment_entry = PriolisteAssignment.objects.get(pk=kwargs['pk'])
            self.finished_until = assignment_entry.finished_until
            try:
                surveyorder = self.order_obj.objects.filter(operation_Number=assignment_entry.ordering_number)\
                    .get(customer_invoice_address__contact_person=assignment_entry.customer)
            except ObjectDoesNotExist:
                return False
            obj = surveyorder
            prod_rec = self.input_obj.objects.filter(order__pk=surveyorder.pk).order_by('pk')
            progress_number = kwargs['progress_number']
        else:
            prod_rec = self.input_obj.objects.filter(order__pk=kwargs['pk']).order_by('pk')
            try:
                self.finished_until = prod_rec[0].finished_until
            except AttributeError:
                pass
            obj = get_object_or_404(self.obj, pk=kwargs['pk'])
        context['date'] = datetime.now()
        context['progress_number'] = progress_number
        context['object'] = obj
        context['finished_until'] = self.finished_until
        context['prod_rec'] = prod_rec
        context['prod_rec_first'] = prod_rec[0]
        context['co_worker'] = prod_rec[0].co_worker
        context['prod_len'] = len(prod_rec)
        context['sum_collar'] = sum([int(i) for i in obj.number_of_collars.split('$')[:-1]])
        context['amount'] = obj.number_of_collars.split('$')[:-1]
        if not self.minifawn:
            try:
                context['sizes'] = obj.nom_collar_circumference.split('$')[:-1]
                context['battery_sizes'] = obj.battery_size.split('$')[:-1]
            except AttributeError:
                pass
        else:
            context['min_circ'] = obj.min_belt_circumference.split('$')[:-1]
            context['max_circ'] = obj.max_belt_circumference.split('$')[:-1]
            context['battery_sizes'] = list(['1C' for i in obj.number_of_collars.split('$')[:-1]])
        if self.test:
            context['test'] = '<span style="font-size:26px; color: chocolate">!!!!!TEST VIEW!!!!!</span>'
        return context

    def get_pdf_response(self, context, **response_kwargs):
        if not context:
            response = redirect(reverse('pListe:home'))
            response['Location'] += '?error'
            return response
        else:
            return super(ProdRecView, self).get_pdf_response(context, **response_kwargs)


class OriginPDFView(PDFView):

    def __init__(self, model, template_name, original=True):
        super(OriginPDFView, self).__init__(model, template_name, original=True)

    def get_context_data(self, **kwargs):
        context = super(OriginPDFView, self).get_context_data(**kwargs)
        obj = self.obj.objects.get(pk=kwargs['pk'])
        origin = dict()
        try:
            keys = [o.split(':')[0].strip() for o in obj.origin.split('§')]
            values = [o.split(':')[1].strip() for o in obj.origin.split('§')]
            origin = dict(zip(keys, values))
        except IndexError:
            pass
        except AttributeError:
            pass
        staff_obj = Staff.objects.get(initialies=obj.customer_staff)
        context['object'] = obj
        try:
            if obj.gsm or obj.gsm is False:
                context['space'] = int(8 - (len(obj.vhf_beacon_frequency)) / 100)
        except AttributeError:
            context['space'] = int(26 - (len(obj.vhf_beacon_frequency)) / 100)
        context['origin'] = origin
        context['customer_mail'] = staff_obj.email
        context['customer_name'] = staff_obj.name
        return context


def prod_rec_print(request, pk):
    prod_rec = SalesSalesinputsurvey.objects.filter(order__pk=pk)
    obj = get_object_or_404(Surveyordermodel, pk=pk)
    context = {
        'date':  datetime.now(),
        'object': obj,
        'prod_rec': prod_rec,
        'prod_rec_first': prod_rec[0],
        'co_worker': prod_rec[0].co_worker,
        'prod_len': len(prod_rec),
        'sum_collar': sum([int(i) for i in obj.number_of_collars.split('$')[:-1]]),
        'amount': obj.number_of_collars.split('$')[:-1],
        'sizes': obj.nom_collar_circumference.split('$')[:-1],
        'battery_sizes': obj.battery_size.split('$')[:-1],
    }

    html_template = get_template('surveyProdTESTRec4Pdf.html')
    html_string = html_template.render(context).encode(encoding="UTF-8")
    html = HTML(base_url='europa:9003', string=html_string)
    html.write_pdf(target=BASE_DIR + '/tmp/' + obj.operation_Number + '.pdf')
    filename = BASE_DIR + '/tmp/' + obj.operation_Number + '.pdf'

    return redirect('sales:listsorders')


def accept_order(request, pk, obj, success_url):
    order = get_object_or_404(obj, pk=pk)
    if order is not None:
        order.order_acceptet = True
        order.save()
        return redirect(reverse(success_url))
    else:
        raise 404


def the_search(request, obj_list, redirect_url, title):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            context = {}
            search_string = form['search_string'].value()
            if search_string == '':
                return redirect(reverse(redirect_url))
            else:
                order_acceptet = True if 'Accepted' in request.path else False
                object_list = [i[0] for i in [searching(o, search_string, **{
                        'foreignKeyFields': ['contact_person', 'delivery_contact_person'],
                        'filter': ('order_acceptet', order_acceptet)

                    }) for o in obj_list]if len(i) > 0]
                if order_acceptet:
                    title = 'Acceptet Orders'
                context = {
                    'list_objects': object_list,
                    'title': title,
                    'form_staffs': StaffChoiceForm,
                    'form_search': SearchForm,
                }

            return render(request, 'list_of_collars.html', context)
        else:
            redirect(reverse(redirect_url))
    else:
        redirect(reverse(redirect_url))


def get_model_objects(acceptet=False):
    list_of_models = [Surveyordermodel, Vertexliteordermodel, Traptransmitterordermodel, Minifawnordermodel]
    objects = []
    for obj in list_of_models:
        objects.append(obj.objects.filter(order_acceptet=acceptet))
    return objects
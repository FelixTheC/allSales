from datetime import date
from staff.models import Staff
from django.views.generic import ListView
from django.views.generic import DeleteView
from survey.models import Surveyordermodel
from django.shortcuts import render, redirect
from django.urls import reverse
from collar.models import Customers
from .forms import LinkCreateForm
from .utils import createHash
from .models import LinkHash
from .utils import PDFView
from vertexLite.models import Vertexliteordermodel
from .utils import accept_order, the_search
from survey.forms import SurveyUpdateForm
from survey.forms import SalesInputSurveyCreateForm
from .forms import StaffChoiceForm
from .forms import SearchForm
from survey.models import SalesSalesinputsurvey
from .utils import ProdRecView
from prioListe.models import PriolisteAssignment
from vertexLite.forms import VertexLiteUpdateForm
from survey.forms import ProdRecCreateForm
from .utils import get_model_objects
from .utils import OriginPDFView
from miniFawn.models import Minifawnordermodel
from trapTransmitter.models import Traptransmitterordermodel
from vertexLite.models import SalesSalesinputvertexlite
from vertexLite.forms import SalesInputVertexLiteCreateForm
from vertexLite.forms import VertexLiteProdRecForm
from miniFawn.forms import MiniFawnUpdateForm
from miniFawn.forms import SalesInputMiniFawnCreateForm
from miniFawn.models import SalesSalesinputminifawn
from miniFawn.forms import MiniFawnProdRecForm
from trapTransmitter.forms import TrapTransmitterUpdateForm
from trapTransmitter.forms import SalesInputTrapTransCreateForm
from trapTransmitter.forms import TrapTransmitterProdRecForm
from trapTransmitter.models import SalesSalesinputtraptransmitter
from .extra import CollarDetailView
from .extra import CreatePrioEntryByOrder
from .extra import production_record_update
from .extra import ProductionRecordInitial
from .extra import CollarUpdateAllFieldsView
from .extra import CreateProductionRecord


def create_link(request):
    context = {}
    if request.method != 'POST':
        context = {
            'form': LinkCreateForm
        }
    else:
        form = LinkCreateForm(request.POST)
        customerMail = form['customerEmail'].value()
        customerId = form['contact_person'].value()
        staffid = form['staff'].value()
        staff = Staff.objects.get(pk=staffid)
        operation_Number = form['operation_Number'].value()
        collarType = form['collarType'].value()
        communicationType = form['communicationType'].value()
        companyType = form['company'].value()
        if form.is_valid():
            linkHash = []
            if collarType == 'Survey':
                linkHash.append('survey/' + create_hash_and_link(Surveyordermodel, staff, staffid, customerId, operation_Number, communicationType, companyType))
            elif collarType == 'VertexLite':
                linkHash.append('vertex_lite/' + create_hash_and_link(Vertexliteordermodel, staff, staffid, customerId, operation_Number, communicationType, companyType))
            elif collarType == 'MiniFawn':
                linkHash.append('miniFawn/' + create_hash_and_link(Minifawnordermodel, staff, staffid, customerId, operation_Number, communicationType, companyType))
            elif collarType == 'TrapTransmitter':
                linkHash.append('trapTransmitter/' + create_hash_and_link(Traptransmitterordermodel, staff, staffid, customerId, operation_Number, communicationType, companyType))
            else:
                pass
                #create_hash_and_link(Vertexordermodel, staff, staffid, customerId)
            context = {
                'link': linkHash,
                'collarType': collarType,
                'customerMail': customerMail
            }
        else:
            context = {
                'form': form,
            }
    return render(request, 'link_create.html', context)


def overview(request):
    return render(request, 'overview.html')


def create_hash_and_link(object, staff, staffid, customerId, operation_Number, communicationType, companyType):
    orderId = pre_create_survey_order_model(object, staffid, customerId, operation_Number, communicationType, companyType)
    linkHash = (createHash() + staff.initialies + str(orderId))
    link = LinkHash.objects.create(hash=linkHash)
    link.save(using='order_db')
    return linkHash


def pre_create_survey_order_model(object, staffid, customerId, operation_Number, communicationType, companyType):
    obj = object()
    obj.as_post = False
    obj.as_email = False
    obj.customer_faktura_id = int(customerId)
    obj.airtime_contract = ''
    try:
        customers = Customers.objects.get(id_customer=customerId)
        obj.contacts_faktura_id = customers.cust_ref_number
    except:
        pass
    obj.same_addr = True
    obj.customer_staff = Staff.objects.get(pk=staffid).initialies
    obj.external_dropoff = False
    if communicationType == 'GL':
        obj.globalstar = True
    else:
        obj.globalstar = False
    if communicationType == 'IR':
        obj.iridium = True
    else:
        obj.iridium = False
    try:
        if communicationType == 'GSM':
            obj.gsm = True
            obj.gsm_vectronic_sim = True
        else:
            obj.gsm = False
    except:
        pass
    try:
        if communicationType == 'SOB':
            obj.store_on_board = True
        else:
            obj.store_on_board = False
    except:
        pass
    obj.belt_labeling = False
    obj.belt_plates = False
    obj.created_at = date.today()
    obj.order_acceptet = False
    try:
        obj.operation_number = operation_Number
    except:
        pass
    obj.operation_Number = operation_Number
    obj.inc_or_gmbh = companyType
    obj.save(using='order_db')
    return obj.pk


def accept_survey_order(request, pk):
    return accept_order(request, pk, Surveyordermodel, 'sales:listsorders')


def accept_vertex_lite_order(request, pk):
    return accept_order(request, pk, Vertexliteordermodel, success_url='sales:listsorders')


def accept_mini_fawn_order(request, pk):
    return accept_order(request, pk, Minifawnordermodel, success_url='sales:listsorders')


def accept_trap_transmitter_order(request, pk):
    return accept_order(request, pk, Traptransmitterordermodel, success_url='sales:listsorders')


def search(request, redirect_url):
    print(request.path)
    if 'Accepted' in request.path:
        new_redirect_url = 'sales:listdoneorders'
        title = 'Accepted Orders'
    else:
        new_redirect_url = 'sales:listsorders'
        title = 'Open Orders'
    try:
        return the_search(request, [Surveyordermodel, Vertexliteordermodel,
                                    Traptransmitterordermodel, Minifawnordermodel], new_redirect_url, title)
    except ValueError:
        return redirect(reverse(new_redirect_url))


def sales_input(request, pk):
    redirect_url = 'sales:listvertexlites'
    form = SalesInputSurveyCreateForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse(redirect_url))


class AllOrders(ListView):
    template_name = 'list_of_collars.html'

    def get_queryset(self):
        return Surveyordermodel.objects.filter(order_acceptet=False)

    def get_context_data(self, **kwargs):
        context = super(AllOrders, self).get_context_data(**kwargs)
        context['form_staffs'] = StaffChoiceForm
        context['form_search'] = SearchForm
        context['title'] = 'Running Orders'
        context['list_objects'] = get_model_objects()
        return context


class AllDoneOrders(AllOrders):
    template_name = 'list_of_collars.html'

    def get_queryset(self):
        return Surveyordermodel.objects.filter(order_acceptet=True)

    def get_context_data(self, **kwargs):
        context = super(AllOrders, self).get_context_data(**kwargs)
        context['form_staffs'] = StaffChoiceForm
        context['form_search'] = SearchForm
        context['title'] = 'Accepted Orders'
        context['list_objects'] = get_model_objects(True)
        return context


class SurveyUpdateView(CollarUpdateAllFieldsView):
    def __init__(self):
        super(SurveyUpdateView, self).__init__(model=Surveyordermodel,
                                               input_model=SalesSalesinputsurvey,
                                               template_name='sellsSurveyForm.html',
                                               form_class=SurveyUpdateForm,
                                               )


class VertexLiteUpdateView(CollarUpdateAllFieldsView):
    def __init__(self):
        super(VertexLiteUpdateView, self).__init__(model=Vertexliteordermodel,
                                                   input_model=SalesSalesinputvertexlite,
                                                   template_name='sellsVertexLiteForm.html',
                                                   form_class=VertexLiteUpdateForm,
                                                   )


class MiniFawnUpdateView(CollarUpdateAllFieldsView):
    def __init__(self):
        super(MiniFawnUpdateView, self).__init__(model=Minifawnordermodel,
                                                 input_model=SalesSalesinputminifawn,
                                                 template_name='sellsMiniFawnForm.html',
                                                 form_class=MiniFawnUpdateForm,
                                                 )


class TrapTransmitterUpdateView(CollarUpdateAllFieldsView):
    def __init__(self):
        super(TrapTransmitterUpdateView, self).__init__(model=Traptransmitterordermodel,
                                                        input_model=SalesSalesinputtraptransmitter,
                                                        template_name='sellsTrapTransForm.html',
                                                        form_class=TrapTransmitterUpdateForm,
                                                        )


class SurveyDetailView(CollarDetailView):
    def __init__(self):
        super(SurveyDetailView, self).__init__(model=Surveyordermodel,
                                               template_name='collarDetail.html')


class VertexLiteDetailView(CollarDetailView):
    def __init__(self):
        super(VertexLiteDetailView, self).__init__(model=Vertexliteordermodel,
                                                   template_name='collarDetail.html')


class MiniFawnDetailView(CollarDetailView):
    def __init__(self):
        super(MiniFawnDetailView, self).__init__(model=Minifawnordermodel,
                                                 template_name='collarDetail.html')


class TrapTransmitterDetailView(CollarDetailView):
    def __init__(self):
        super(TrapTransmitterDetailView, self).__init__(model=Traptransmitterordermodel,
                                                 template_name='collarDetail.html')


class SurveyPDFView(PDFView):
    def __init__(self):
        super(SurveyPDFView, self).__init__(obj=Surveyordermodel,
                                            template_name='surveyHtml4Pdf.html')


class VertexLitePDFView(PDFView):
    def __init__(self):
        super(VertexLitePDFView, self).__init__(obj=Vertexliteordermodel,
                                                template_name='vertexLiteFinalOrderPdf.html')


class MiniFawnPDFView(PDFView):
    def __init__(self):
        super(MiniFawnPDFView, self).__init__(obj=Minifawnordermodel,
                                              template_name='miniFawnFinalOrderPdf.html')


class TrapTransPDFView(PDFView):
    def __init__(self):
        super(TrapTransPDFView, self).__init__(obj=Traptransmitterordermodel,
                                               template_name='trapTransFinalOrderPdf.html')


class SurveyOriginPDFView(OriginPDFView):
    def __init__(self):
        super(SurveyOriginPDFView, self).__init__(model=Surveyordermodel,
                                                  template_name='surveyOriginHtml4Pdf.html')


class VertexLiteOriginPDFView(OriginPDFView):
    def __init__(self):
        super(VertexLiteOriginPDFView, self).__init__(model=Vertexliteordermodel,
                                                      template_name='vertexLiteOriginOrderPdf.html')


class MiniFawnOriginPDFView(OriginPDFView):
    def __init__(self):
        super(MiniFawnOriginPDFView, self).__init__(model=Minifawnordermodel,
                                                    template_name='miniFawnOriginOrderPdf.html')


class TrapTransOriginPDFView(OriginPDFView):
    def __init__(self):
        super(TrapTransOriginPDFView, self).__init__(model=Traptransmitterordermodel,
                                                    template_name='trapTransOriginOrderPdf.html')


class ProdRecPDFView(ProdRecView):
    def __init__(self):
        super(ProdRecPDFView, self).__init__(obj=Surveyordermodel,
                                             template_name='prod_rec_main.html',
                                             test=True,
                                             order_obj=Surveyordermodel,
                                             input_obj=SalesSalesinputsurvey,
                                             from_prio=False,
                                             )


class VtxlProdRecPDFView(ProdRecView):
    def __init__(self):
        super(VtxlProdRecPDFView, self).__init__(obj=Vertexliteordermodel,
                                                 template_name='prod_rec_vtxl.html',
                                                 test=True,
                                                 order_obj=Vertexliteordermodel,
                                                 input_obj=SalesSalesinputvertexlite,
                                                 from_prio=False,
                                                 )


class MfProdRecPDFView(ProdRecView):
    def __init__(self):
        super(MfProdRecPDFView, self).__init__(obj=Minifawnordermodel,
                                               template_name='prod_rec_mf.html',
                                               test=True,
                                               order_obj=Minifawnordermodel,
                                               input_obj=SalesSalesinputminifawn,
                                               from_prio=False,
                                               minifawn=True
                                               )


class TrapTransProdRecPDFView(ProdRecView):
    def __init__(self):
        super(TrapTransProdRecPDFView, self).__init__(obj=Traptransmitterordermodel,
                                                      template_name='prod_rec_tt3.html',
                                                      test=True,
                                                      order_obj=Traptransmitterordermodel,
                                                      input_obj=SalesSalesinputtraptransmitter,
                                                      from_prio=False,
                                                      )


class ProdRecFromPrioListePDFView(ProdRecView):
    def __init__(self):
        super(ProdRecFromPrioListePDFView, self).__init__(obj=PriolisteAssignment,
                                                          template_name='prod_rec_main.html',
                                                          from_prio=True,
                                                          order_obj=Surveyordermodel,
                                                          input_obj=SalesSalesinputsurvey,
                                                          )


class SurveyProductionRecord(CreateProductionRecord):
    def __init__(self):
        super(SurveyProductionRecord, self).__init__(model=SalesSalesinputsurvey,
                                                     order_model=Surveyordermodel,
                                                     form_class=SalesInputSurveyCreateForm,
                                                     template_name='surveyProdRec.html')


class VertexLiteProductionRecord(CreateProductionRecord):
    def __init__(self):
        super(VertexLiteProductionRecord, self).__init__(model=SalesSalesinputvertexlite,
                                                         order_model=Vertexliteordermodel,
                                                         form_class=SalesInputVertexLiteCreateForm,
                                                         template_name='surveyProdRec.html')


class MiniFawnProductionRecord(CreateProductionRecord):
    def __init__(self):
        super(MiniFawnProductionRecord, self).__init__(model=SalesSalesinputminifawn,
                                                       order_model=Minifawnordermodel,
                                                       form_class=SalesInputMiniFawnCreateForm,
                                                       template_name='surveyProdRec.html')


class TrapTransmitterProductionRecord(CreateProductionRecord):
    def __init__(self):
        super(TrapTransmitterProductionRecord, self).__init__(model=SalesSalesinputtraptransmitter,
                                                              order_model=Traptransmitterordermodel,
                                                              form_class=SalesInputTrapTransCreateForm,
                                                              template_name='surveyProdRec.html')


class SurveyProductionRecordInitial(ProductionRecordInitial):
    def __init__(self):
        super(SurveyProductionRecordInitial, self).__init__(model=SalesSalesinputsurvey,
                                                            order_model=Surveyordermodel,
                                                            form_class=ProdRecCreateForm,
                                                            template='surveyProdRec.html')


class VertexLiteProductionRecordInitial(ProductionRecordInitial):
    def __init__(self):
        super(VertexLiteProductionRecordInitial, self).__init__(model=SalesSalesinputvertexlite,
                                                                order_model=Vertexliteordermodel,
                                                                form_class=VertexLiteProdRecForm,
                                                                template='surveyProdRec.html')


class MiniFawnProductionRecordInitial(ProductionRecordInitial):
    def __init__(self):
        super(MiniFawnProductionRecordInitial, self).__init__(model=SalesSalesinputminifawn,
                                                              order_model=Minifawnordermodel,
                                                              form_class=MiniFawnProdRecForm,
                                                              template='surveyProdRec.html')


class TrapTransmitterProductionRecordInitial(ProductionRecordInitial):
    def __init__(self):
        super(TrapTransmitterProductionRecordInitial, self).__init__(model=SalesSalesinputtraptransmitter,
                                                                     order_model=Traptransmitterordermodel,
                                                                     form_class=TrapTransmitterProdRecForm,
                                                                     template='surveyProdRec.html')


# class SurveyProductionRecordUpdate(ProductionRecordUpdate):
#     def __init__(self):
#         super(SurveyProductionRecordUpdate, self).__init__(model=SalesSalesinputsurvey,
#                                                            order_model=Surveyordermodel,
#                                                            form_class=SalesInputSurveyCreateForm,
#                                                            template='sellsSurveyForm.html')


class SurveyModelDelete(DeleteView):
    def __init__(self):
        super(SurveyModelDelete, self).__init__(model=Surveyordermodel)


class VertexLiteModelDelete(DeleteView):
    def __init__(self):
        super(VertexLiteModelDelete, self).__init__(model=Vertexliteordermodel)


class MiniFawnModelDelete(DeleteView):
    def __init__(self):
        super(MiniFawnModelDelete, self).__init__(model=Minifawnordermodel)


class TrapTransmitterModelDelete(DeleteView):
    def __init__(self):
        super(TrapTransmitterModelDelete, self).__init__(model=Traptransmitterordermodel)


class CreateSurveyPrioEntryByOrder(CreatePrioEntryByOrder):

    def get_hardware_string(self):
        order = self.order
        try:
            numbers_of_collars = order.number_of_collars.split('$')
            battery_size = order.battery_size.split('$')
            hardware_string = ''
            for i in range(len(numbers_of_collars) - 1):
                if order.iridium:
                    if order.external_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Survey IR {battery_size[i]} mit DO<br>'
                    else:
                        hardware_string += f'{numbers_of_collars[i]}x Survey IR {battery_size[i]} <br>'
                else:
                    if order.external_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Survey GL {battery_size[i]} mit DO<br>'
                    else:
                        hardware_string += f'{numbers_of_collars[i]}x Survey GL {battery_size[i]} <br>'
        except AttributeError:
            hardware_string = ''
        return hardware_string

    def __init__(self):
        super(CreateSurveyPrioEntryByOrder, self).__init__(order_model=Surveyordermodel,
                                                           hardware_string=self.get_hardware_string)


class CreateVertexLitePrioEntryByOrder(CreatePrioEntryByOrder):

    def get_hardware_string(self):
        order = self.order
        try:
            numbers_of_collars = order.number_of_collars.split('$')
            battery_size = order.battery_size.split('$')
            hardware_string = ''
            for i in range(len(numbers_of_collars) - 1):
                if order.iridium:
                    if order.external_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite IR {battery_size[i]} mit ext DO<br>'
                    elif order.internal_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite IR {battery_size[i]} mit DO<br>'
                    elif order.store_on_board:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite IR {battery_size[i]} mit store on board DO<br>'
                    else:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite IR {battery_size[i]} <br>'
                elif order.gsm:
                    if order.external_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GSM {battery_size[i]} mit ext DO<br>'
                    elif order.internal_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GSM {battery_size[i]} mit DO<br>'
                    elif order.store_on_board:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GSM {battery_size[i]} mit store on board DO<br>'
                    else:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GSM {battery_size[i]} <br>'
                else:
                    if order.external_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GL {battery_size[i]} mit ext DO<br>'
                    elif order.internal_dropoff:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GL {battery_size[i]} mit DO<br>'
                    elif order.store_on_board:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GL {battery_size[i]} mit store on board DO<br>'
                    else:
                        hardware_string += f'{numbers_of_collars[i]}x Vertex Lite GL {battery_size[i]} <br>'
        except AttributeError:
            hardware_string = ''
        return hardware_string

    def __init__(self):
        super(CreateVertexLitePrioEntryByOrder, self).__init__(order_model=Vertexliteordermodel,
                                                               hardware_string=self.get_hardware_string)


class CreateMiniFawnPrioEntryByOrder(CreatePrioEntryByOrder):

    def get_hardware_string(self):
        order = self.order
        try:
            numbers_of_collars = order.number_of_collars.split('$')
            battery_size = order.battery_size.split('$')
            hardware_string = ''
            for i in range(len(numbers_of_collars) - 1):
                 hardware_string += f'{numbers_of_collars[i]}x Mini Fawn GL {battery_size[i]} <br>'
        except AttributeError:
            hardware_string = ''
        return hardware_string

    def __init__(self):
        super(CreateMiniFawnPrioEntryByOrder, self).__init__(order_model=Minifawnordermodel,
                                                             hardware_string=self.get_hardware_string)


class CreateTrapTransmitterPrioEntryByOrder(CreatePrioEntryByOrder):

    def get_hardware_string(self):
        order = self.order
        try:
            numbers_of_collars = order.number_of_collars.split('$')
            battery_size = order.battery_size.split('$')
            hardware_string = ''
            for i in range(len(numbers_of_collars) - 1):
                if order.iridium:
                    hardware_string += f'{numbers_of_collars[i]}x TT3 IR {battery_size[i]} <br>'
                else:
                    hardware_string += f'{numbers_of_collars[i]}x TT3 GS {battery_size[i]} <br>'

        except AttributeError:
            hardware_string = ''
        return hardware_string

    def __init__(self):
        super(CreateTrapTransmitterPrioEntryByOrder, self).__init__(order_model=Traptransmitterordermodel,
                                                                    hardware_string=self.get_hardware_string)


def survey_production_record_update(request, pk):
    return production_record_update(request, pk, SalesSalesinputsurvey, 'updatesurveys')


def vertex_lite_production_record_update(request, pk):
    return production_record_update(request, pk, SalesSalesinputvertexlite, 'updatesurveys')


def mini_fawn_production_record_update(request, pk):
    return production_record_update(request, pk, SalesSalesinputminifawn, 'updatesurveys')


def trap_trans_production_record_update(request, pk):
    return production_record_update(request, pk, SalesSalesinputtraptransmitter, 'updatesurveys')

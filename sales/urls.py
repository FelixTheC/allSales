from django.conf.urls import url
from . import views
from . import utils
from .views import AllOrders
from .views import AllDoneOrders
from .views import SurveyDetailView
from .views import VertexLiteDetailView
from .views import MiniFawnDetailView
from .views import TrapTransmitterDetailView
from .views import SurveyUpdateView
from .views import VertexLiteUpdateView
from .views import MiniFawnUpdateView
from .views import TrapTransmitterUpdateView
from .views import SurveyPDFView
from .views import SurveyOriginPDFView
from .views import SurveyProductionRecord
from .views import VertexLiteProductionRecord
from .views import MiniFawnProductionRecord
from .views import TrapTransmitterProductionRecord
from .views import SurveyProductionRecordInitial
from .views import VertexLiteProductionRecordInitial
from .views import MiniFawnProductionRecordInitial
from .views import TrapTransmitterProductionRecordInitial
from .views import ProdRecPDFView
from .views import VtxlProdRecPDFView
from .views import MfProdRecPDFView
from .views import TrapTransProdRecPDFView
from .views import VertexLitePDFView
from .views import VertexLiteOriginPDFView
from .views import MiniFawnPDFView
from .views import MiniFawnOriginPDFView
from .views import TrapTransPDFView
from .views import TrapTransOriginPDFView
from .views import CreateSurveyPrioEntryByOrder
from .views import CreateVertexLitePrioEntryByOrder
from .views import CreateMiniFawnPrioEntryByOrder
from .views import CreateTrapTransmitterPrioEntryByOrder
from .views import ProdRecFromPrioListePDFView
from .views import SurveyModelDelete
from .views import VertexLiteModelDelete
from .views import MiniFawnModelDelete
from .views import TrapTransmitterModelDelete


app_name = 'sales'
urlpatterns = [
    url(r'^$', views.overview, name='overview'),
    url(r'^link/', views.create_link, name='createLink'),
    ############
    #Lists
    ############
    url(r'^list-open-orders/', AllOrders.as_view(), name='listsorders'),
    url(r'^list-done-orders/', AllDoneOrders.as_view(), name='listdoneorders'),
    ############
    #Detail View
    ############
    url(r'^detail-surveys/(?P<pk>[\d]+)/$', SurveyDetailView.as_view(), name='detailsurveys'),
    url(r'^detail-vertex-lite/(?P<pk>[\d]+)/$', VertexLiteDetailView.as_view(), name='detailvertexlite'),
    url(r'^detail-mini_fawn/(?P<pk>[\d]+)/$', MiniFawnDetailView.as_view(), name='detailminifawn'),
    url(r'^detail-trap_trans/(?P<pk>[\d]+)/$', TrapTransmitterDetailView.as_view(), name='detailtraptrans'),
    ############
    #Update View
    ############
    url(r'^update-surveys/(?P<pk>[\d]+)/$', SurveyUpdateView.as_view(), name='updatesurveys'),
    url(r'^update-vertex-lite/(?P<pk>[\d]+)/$', VertexLiteUpdateView.as_view(), name='updatevertexlite'),
    url(r'^update-mini-fawn/(?P<pk>[\d]+)/$', MiniFawnUpdateView.as_view(), name='updateminifawn'),
    url(r'^update-trap-trans/(?P<pk>[\d]+)/$', TrapTransmitterUpdateView.as_view(), name='updatetraptrans'),
    ############
    #Instant Accept
    ############
    url(r'^accept-survey/(?P<pk>[\d]+)/$', views.accept_survey_order, name='acceptsurvey'),
    url(r'^accept-vertex-lite/(?P<pk>[\d]+)/$', views.accept_vertex_lite_order, name='acceptvertexlite'),
    url(r'^accept-mini-fawn/(?P<pk>[\d]+)/$', views.accept_mini_fawn_order, name='acceptminifawn'),
    url(r'^accept-trap-trans/(?P<pk>[\d]+)/$', views.accept_trap_transmitter_order, name='accepttraptrans'),
    ############
    #Write into prioList
    ############
    url(r'^accept-survey-write-prioliste/(?P<pk>[\d]+)/$', CreateSurveyPrioEntryByOrder.as_view(),
        name='acceptsurveywriteprioliste'),
    url(r'^accept-vtxl-write-prioliste/(?P<pk>[\d]+)/$', CreateVertexLitePrioEntryByOrder.as_view(),
        name='acceptvertexlitewriteprioliste'),
    url(r'^accept-mf-write-prioliste/(?P<pk>[\d]+)/$', CreateMiniFawnPrioEntryByOrder.as_view(),
        name='acceptminifawnwriteprioliste'),
    url(r'^accept-tt-write-prioliste/(?P<pk>[\d]+)/$', CreateTrapTransmitterPrioEntryByOrder.as_view(),
        name='accepttraptranswriteprioliste'),
    ############
    #Pdf File
    ############
    url(r'^surveys-order-pdf/(?P<pk>[\d]+)/$', SurveyPDFView.as_view(), name='surveyorderpdf'),
    url(r'^surveys-origin-pdf/(?P<pk>[\d]+)/$', SurveyOriginPDFView.as_view(), name='surveyoriginpdf'),
    url(r'^vertex-lite-order-pdf/(?P<pk>[\d]+)/$', VertexLitePDFView.as_view(), name='vertexliteorderpdf'),
    url(r'^vertex-lite-origin-pdf/(?P<pk>[\d]+)/$', VertexLiteOriginPDFView.as_view(), name='vertexliteoriginpdf'),
    url(r'^mini-fawn-order-pdf/(?P<pk>[\d]+)/$', MiniFawnPDFView.as_view(), name='minifawnorderpdf'),
    url(r'^mini-fawn-origin-pdf/(?P<pk>[\d]+)/$', MiniFawnOriginPDFView.as_view(), name='minifawnoriginpdf'),
    url(r'^trap-trans-order-pdf/(?P<pk>[\d]+)/$', TrapTransPDFView.as_view(), name='traptransorderpdf'),
    url(r'^trap-trans-origin-pdf/(?P<pk>[\d]+)/$', TrapTransOriginPDFView.as_view(), name='traptransoriginpdf'),
    ############
    #ProdRecordsPdf
    ############
    url(r'^prod-rec-survey-pdf/(?P<pk>[\d]+)/$', ProdRecPDFView.as_view(), name='prodrecpdf'),
    url(r'^prod-rec-vtxl-pdf/(?P<pk>[\d]+)/$', VtxlProdRecPDFView.as_view(), name='vtxlprodrecpdf'),
    url(r'^prod-rec-minf-pdf/(?P<pk>[\d]+)/$', MfProdRecPDFView.as_view(), name='mfprodrecpdf'),
    url(r'^prod-rec-ttr-pdf/(?P<pk>[\d]+)/$', TrapTransProdRecPDFView.as_view(), name='traptransprodrecpdf'),
    url(r'^prod-rec-pdf/(?P<pk>[\d]+)/(?P<progress_number>[\d]+)/$', ProdRecFromPrioListePDFView.as_view(),
        name='prodrecpdf_fromprioliste'),
    url(r'^print-prod-rec-pdf/(?P<pk>[\d]+)/$', utils.prod_rec_print, name='printprodrecpdf'),
    ############
    #Search and filter views
    ############
    url(r'^search/(?P<redirect_url>.*)/$', views.search, name='search'),
    ############
    #ProdRecords
    ############
    url(r'^survey-prod-rec/(?P<pk>[\d]+)/$', SurveyProductionRecord.as_view(), name='prodrec'),
    url(r'^vl-prod-rec/(?P<pk>[\d]+)/$', VertexLiteProductionRecord.as_view(), name='vlprodrec'),
    url(r'^mf-prod-rec/(?P<pk>[\d]+)/$', MiniFawnProductionRecord.as_view(), name='mfprodrec'),
    url(r'^tt-prod-rec/(?P<pk>[\d]+)/$', TrapTransmitterProductionRecord.as_view(), name='ttprodrec'),
    url(r'^initial-survey-prod-rec/(?P<pk>[\d]+)/$', SurveyProductionRecordInitial.as_view(), name='initialprodrec'),
    url(r'^initial-vtxl-prod-rec/(?P<pk>[\d]+)/$', VertexLiteProductionRecordInitial.as_view(), name='vtxlinitialprodrec'),
    url(r'^initial-mf-prod-rec/(?P<pk>[\d]+)/$', MiniFawnProductionRecordInitial.as_view(), name='mfinitialprodrec'),
    url(r'^initial-tt-prod-rec/(?P<pk>[\d]+)/$', TrapTransmitterProductionRecordInitial.as_view(), name='ttinitialprodrec'),
    url(r'^prod-rec-update/(?P<pk>[\d]+)/$', views.survey_production_record_update, name='updateprodrec'),
    url(r'^prod-rec-update/(?P<pk>[\d]+)/$', views.vertex_lite_production_record_update, name='updateprodrecvtxl'),
    url(r'^prod-rec-update/(?P<pk>[\d]+)/$', views.mini_fawn_production_record_update, name='updateprodrecmf'),
    url(r'^prod-rec-update/(?P<pk>[\d]+)/$', views.trap_trans_production_record_update, name='updateprodrectraptrans'),
    ############
    #Delete View
    ############
    url(r'^delete/(?P<pk>[\d]+)/$', SurveyModelDelete.as_view(), name='surveydelete'),
    url(r'^delete/(?P<pk>[\d]+)/$', VertexLiteModelDelete.as_view(), name='vertexlitedelete'),
    url(r'^delete/(?P<pk>[\d]+)/$', MiniFawnModelDelete.as_view(), name='minifawndelete'),
    url(r'^delete/(?P<pk>[\d]+)/$', TrapTransmitterModelDelete.as_view(), name='traptransdelete'),
]
from django.conf.urls import url
from django.conf.urls.static import static

from allSales import settings
from . import views
from .views import RefurbishmentFormView
from .views import RefurbishmentUpdateView
from .views import RMADelete

app_name = 'rma'
urlpatterns = [
    url(r'^$', views.refurbishment_list, name='home'),
    url(r'^create/$', RefurbishmentFormView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\d]+)$', RefurbishmentUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[\d+]+)$', RMADelete.as_view(), name='delete'),
    url(r'^search/$', views.search_customer, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
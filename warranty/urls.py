from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from .views import WarrantyFormView
from .views import WarrantyList
from .views import WarrantyUpdateView
from .views import WarrantyDelete

app_name = 'warranty'
urlpatterns = [
    url(r'^$', WarrantyList.as_view(), name='home'),
    url(r'^create/$', WarrantyFormView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\d]+)$', WarrantyUpdateView.as_view(), name='update'),
    url(r'^save_delete/(?P<pk>[\d]+)$', WarrantyDelete.as_view(), name='save_delete'),
    url(r'^search/$', views.search_customer, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
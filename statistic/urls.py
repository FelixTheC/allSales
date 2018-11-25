from django.conf.urls import url

from . import views

app_name='statistic'
urlpatterns = [
    url(r'^rma/', views.test_statistic, name='main'),
    url(r'^warranty/', views.warranty_statistic, name='statistic_warranty'),
    url(r'^shippings/', views.delivery_statistics, name='statistic_shippings'),
]
from django.conf.urls import url
from . import views
from .views import UpdateAssignment
from .views import UpdatedProduction
from .views import UpdateAssignmentWithoutBox
from .views import UpdateDoneAssignment

app_name = 'pListe'
urlpatterns = [
    url(r'^prioListe/', views.show_list, name='home'),
    url(r'^missingbelts/$', views.show_missing_belts, name='belts'),
    url(r'^missingbatteries/$', views.show_missing_batteries, name='batterie'),
    url(r'^create/$', views.create_assignment_entry, name='create'),
    url(r'^update/(?P<pk>[\d]+)/$', UpdateAssignment.as_view(), name='update'),
    url(r'^update_withou_box/(?P<pk>[\d]+)/$', UpdateAssignmentWithoutBox.as_view(), name='update_without_box'),
    url(r'^update_box/(?P<pk>[\d]+)/$', views.update_box, name='update_box'),
    url(r'^update_belt/(?P<pk>[\d]+)/(?P<path>.*)/$', views.update_belt, name='update_belt'),
    url(r'^update_batterie/(?P<pk>[\d]+)/(?P<path>.*)/$', views.update_batterie, name='update_batterie'),
    url(r'^update_assembled/(?P<pk>[\d]+)/(?P<path>.*)/$', views.update_assembled, name='update_assembled'),
    url(r'^update_electric/(?P<pk>[\d]+)/(?P<path>.*)/$', views.update_electronic, name='update_electric'),
    url(r'^updateProduction/(?P<pk>[\d]+)/$', UpdatedProduction.as_view(), name='updateProduction'),
    url(r'^batterie/(?P<path>.*)/$', views.show_specifc_batterie_type, name='hardware_batterie'),
    url(r'^update_batterie_shelf/(?P<pk>[\d]+)/$', views.update_batterie_shelf, name='update_batterie_shelf'),
    url(r'^update_belt_shelf/(?P<pk>[\d]+)/$', views.update_belt_shelf, name='update_belt_shelf'),
    url(r'^update_electric_shelf/(?P<pk>[\d]+)/$', views.update_electric_shelf, name='update_electric_shelf'),
    url(r'^search_all/(?P<path>.*)/$', views.search_form, name='prio_search'),
    url(r'^prioListe_done', views.show_finished_list, name='done'),
    url(r'^update_comment/(?P<pk>[\d]+)/$', UpdateDoneAssignment.as_view(), name='update_comment_only'),
    url(r'^notice_delete/(?P<pk>[\d]+)/$', views.notice_about_delete, name='delete_notice')
]

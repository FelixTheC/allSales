from django.db import models
from datetime import datetime

from django.urls import reverse

from staff.models import Staff

from .utils import get_choices
from .utils import COLORS
from .utils import STAFFCHOICESONE


def upload_record_path(instance, filename):
    if instance.ordering_number is not None:
        return '/'.join(['media', instance.ordering_number, filename])
    else:
        return '/'.join(['media', instance.staff + str(instance.internal_progress_number), filename])


class StaffColor(models.Model):
    class Meta:
        managed = True
        app_label = 'prioListe'

    name = models.CharField(max_length=255, choices=STAFFCHOICESONE)
    color = models.CharField(max_length=255, null=False, blank=False, default='#000000')


class PriolisteAssignment(models.Model):
    class Meta:
        ordering = ['finished_until']
        managed = True
        app_label = 'prioListe'

    status = models.CharField(max_length=20, choices=get_choices(), blank=True, null=True)
    finished_until = models.DateField(null=True)
    staff = models.CharField(max_length=10, null=False)
    co_worker = models.CharField(max_length=10, null=False, blank=True)
    time_in_weeks = models.IntegerField(null=True)
    box = models.CharField(max_length=255, null=True, blank=True, help_text='Not longer required')
    customer = models.CharField(max_length=255, null=True)
    hardware = models.TextField(null=True, blank=True)
    optional_status = models.CharField(max_length=200, null=True, blank=True)
    production_remark = models.TextField(null=True, blank=True)
    changed = models.BooleanField(default=False)
    remark = models.TextField(null=True, blank=True)
    assembled = models.BooleanField(default=False, blank=True)
    batterie = models.BooleanField(default=False, blank=True)
    belt = models.BooleanField(default=False, blank=True)
    elektronic = models.BooleanField(default=False, blank=True)
    drop_off = models.BooleanField(default=False, blank=True)
    last_change = models.DateField(blank=True, null=True)
    created_at = models.DateField(default=datetime.today())
    ordering_number = models.CharField(max_length=255, blank=True, null=True)
    internal_progress_number = models.PositiveIntegerField(default=-1)
    prod_rec_one = models.FileField(blank=True, null=True, upload_to=upload_record_path)
    prod_rec_two = models.FileField(blank=True, null=True, upload_to=upload_record_path)
    prod_rec_three = models.FileField(blank=True, null=True, upload_to=upload_record_path)
    prod_rec_four = models.FileField(blank=True, null=True, upload_to=upload_record_path)
    prod_rec_five = models.FileField(blank=True, null=True, upload_to=upload_record_path)
    prod_rec_string = models.CharField(max_length=300, blank=True, null=True)
    has_box = models.BooleanField(default=False, blank=True)
    changed_by_ip = models.CharField(max_length=255, default='0.0.0.0')
    ids = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.ordering_number)

    def get_main_root(self):
        return reverse('pListe:home')

    def get_labelname(self):
        return 'To Priority-List'

    def get_second_root(self):
        return reverse('pListe:done')

    def get_second_labelname(self):
        return 'To Shippingboard'

    def get_update_url(self):
        return reverse('pListe:update', kwargs={
            'pk': self.pk,
        })

    def get_box_update_url(self):
        return reverse('pListe:update_box', kwargs={
            'pk': self.pk,
        })

    def get_box_update_number_url(self):
        return reverse('pListe:update_box_number', kwargs={
            'pk': self.pk,
        })

    def get_update_without_box(self):
        return reverse('pListe:update_without_box', kwargs={
            'pk': self.pk,
        })

    def get_update_production(self):
        return reverse('pListe:updateProduction', kwargs={
            'pk': self.pk,
        })

    def get_shelf(self):
        return Shelf.objects.filter(assignment=self)

    def update_batterie_shelf(self):
        return reverse('pListe:update_batterie_shelf', kwargs={
            'pk': self.pk,
        })

    def update_belt_shelf(self):
        return reverse('pListe:update_belt_shelf', kwargs={
            'pk': self.pk,
        })

    def update_electric_shelf(self):
        return reverse('pListe:update_electric_shelf', kwargs={
            'pk': self.pk,
        })

    def create_productionrecord_reversed(self):
        return reverse('sales:prodrecpdf_fromprioliste', kwargs={
            'pk': self.pk,
            'progress_number': self.internal_progress_number,
        })

    def get_comment_update_only(self):
        return reverse('pListe:update_comment_only', kwargs={
            'pk': self.pk,
        })

    def get_delete_notice(self):
        return reverse('pListe:delete_notice', kwargs={
            'pk': self.pk,
        })

    def get_color(self):
        '''
        :return:
        '''
        color = '#ffffff'
        optional_stat = 'in Bearbeitung'
        choices = [i[0] for i in get_choices()]
        if self.status in choices:
            color = COLORS[self.status]
        elif self.optional_status is not None:
            if self.optional_status in optional_stat:
                color = COLORS['Bearbeitung']
        return color

    def get_staff_color(self):
        staff_color = StaffColor.objects.get(name=self.staff)
        return staff_color.color


class Shelf(models.Model):
    class Meta:
        managed = True
        app_label = 'prioListe'
    shelf_type = models.CharField(max_length=100)
    compartment = models.CharField(max_length=255, blank=True, null=True)
    assignment = models.ForeignKey(PriolisteAssignment)


class ProductionTime(models.Model):
    class Meta:
        managed = True
        app_label = 'prioListe'
    time_in_weeks = models.IntegerField(default=12)
    enabled = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
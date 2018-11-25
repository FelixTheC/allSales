from datetime import datetime

from django.db import models
from django.urls import reverse

from collar.models import Staff

CHOICES = [
    ('', ''),
]
for staff in Staff.objects.all():
    CHOICES.append((staff.name, staff.name))


def file_upload_path(instance, filename):
    return '/'.join(['media', instance.salesPerson, filename])


class Status(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'status'
        app_label = 'rma'


class RMAFile(models.Model):
    rma_file = models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d')

    class Meta:
        db_table = 'rmafiles'
        app_label = 'rma'


class Refurbisment(models.Model):
    rma = models.TextField(max_length=200)
    salesPerson = models.CharField(max_length=100, choices=CHOICES)
    customer_forename = models.TextField(max_length=200, default='Forename')
    customer_name = models.TextField(max_length=200, default='Surname')
    customer_email = models.EmailField()
    country = models.TextField(max_length=200)
    content = models.TextField(max_length=750, null=True, blank=True)
    parcel_received = models.DateField(blank=True, default=datetime.strptime('2000-01-01', '%Y-%m-%d'))
    comments = models.TextField(max_length=750, null=True, blank=True)
    status = models.ForeignKey(to=Status)
    rma_file = models.FileField(null=True, blank=True, upload_to=file_upload_path)
    rma_second_file = models.FileField(null=True, blank=True, upload_to=file_upload_path)
    shelf = models.PositiveIntegerField(null=True, blank=True)
    #more_files = models.CharField(null=True, blank=True, max_length=255)

    def get_update_url(self):
        return reverse('rma:update',
                       kwargs={'pk': self.pk})

    def get_main_root(self):
        return reverse('rma:home')

    def get_labelname(self):
        return 'To RMA-List'

    def get_delete_url(self):
        return reverse('rma:delete', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'refurbisment'
        ordering = ['status']
        app_label = 'rma'
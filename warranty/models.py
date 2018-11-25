from customer.models import Vasdevice
from allSales.settings import MEDIA_ROOT
from django.core.files import File
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime

from collar.models import Staff

staffs = Staff.objects.all()

STAFFCHOICES = [
    ('', ''),
]
for staff in staffs:
    STAFFCHOICES.append((staff.name, staff.name))


def file_upload_path(instance, filename):
    return '/'.join(['media', instance.contact_person.name, filename])


# Create your models here.
class Warranty(models.Model):
    class Meta:
        app_label = 'warranty'
        managed = True
        ordering = ['-date']

    date = models.DateField(default=datetime.today())
    contact_person = models.ForeignKey(Staff, null=True)
    customer_collar = models.ManyToManyField(Vasdevice, null=True, blank=True)
    comment = models.TextField(max_length=200)
    date_delivery = models.TextField(max_length=200)
    date_complaint = models.TextField(max_length=200)
    date_collar_failure = models.TextField(max_length=200)
    description_failure = models.TextField(max_length=255)
    following_action = models.TextField(max_length=255)
    replacement = models.TextField(max_length=100)
    deleted = models.BooleanField(default=False)
    warranty_file = models.FileField(null=True, blank=True, upload_to=file_upload_path)
    lifetime = models.CharField(blank=True, null=True, max_length=255, editable=False)
    # failure_describtion = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.description_failure

    def get_main_root(self):
        return reverse('warranty:home')

    def get_labelname(self):
        return 'To Warranty-List'

    def get_update_url(self):
        return reverse('warranty:update',
                       kwargs={'pk': self.pk})

    def get_update_deleted_url(self):
        return reverse('warranty:save_delete',
                       kwargs={'pk': self.pk})

    def get_customer_collar(self):
        liste = list()
        if self.customer_collar is not None and 'test' not in self.description_failure:
            collars = self.customer_collar.all()
            for collar in collars:
                liste.append(collar.producttype)
        return liste

    def save(self, *args, **kwargs):
        if '-' in self.date_delivery:
            self.date_delivery = self.date_delivery.replace('-', '.')
        if '-' in self.date_collar_failure:
            self.date_collar_failure = self.date_collar_failure.replace('-', '.')
        try:
            days_ = datetime.strptime(self.date_collar_failure, '%d.%m.%Y') - datetime.strptime(self.date_delivery, '%d.%m.%Y')
            days = str(days_).split(' ')
            if int(days[0])//365 > 0 :
                lifetime = f'{int(days[0])//365} yrs, {int(days[0])%365} days'
            else:
                lifetime = f'{days[0]} days'
            self.lifetime = lifetime
        except ValueError:
            pass
        super(Warranty, self).save(*args, **kwargs)
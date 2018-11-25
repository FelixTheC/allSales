from django.db import models
from django.urls import reverse


class Ordercontactdeliveryaddresse(models.Model):
    delivery_organisation_name = models.CharField(max_length=255, blank=True, null=True)
    delivery_complete_addresse = models.CharField(max_length=255, blank=True, null=True)
    delivery_zip_code = models.CharField(max_length=15, blank=True, null=True)
    delivery_city = models.CharField(max_length=255, blank=True, null=True)
    delivery_country = models.CharField(max_length=255, blank=True, null=True)
    delivery_contact_person = models.CharField(max_length=255, blank=True, null=True)
    delivery_email_addresse = models.CharField(max_length=254, blank=True, null=True)
    delivery_telephone_nr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'sales'
        db_table = 'orderContact_ordercontactdeliveryaddresse'

    def __str__(self):
        return self.delivery_organisation_name

    def get_update_link(self):
        return reverse('collar:orderdeliveryaddressupdate', kwargs={'pk': self.pk})


class Ordercontactinvoiceaddresse(models.Model):
    organisation_name = models.CharField(max_length=255, blank=True, null=True)
    complete_addresse = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email_addresse = models.CharField(max_length=254, blank=True, null=True)
    telephone_nr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'sales'
        db_table = 'orderContact_ordercontactinvoiceaddresse'

    def __str__(self):
        return self.organisation_name

    def get_update_link(self):
        return reverse('collar:orderinvoiceaddressupdate', kwargs={'pk': self.pk})

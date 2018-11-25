# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class ContactDetailTypes(models.Model):
    id_contact_detail_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'contact_detail_types'


class ContactDetails(models.Model):
    id_contact_detail = models.AutoField(primary_key=True)
    detail = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id_contact_detail_type = models.ForeignKey(ContactDetailTypes, models.DO_NOTHING, db_column='id_contact_detail_type', blank=True, null=True)
    id_contact = models.ForeignKey('Contacts', models.DO_NOTHING, db_column='id_contact', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_details'


class ContactTypes(models.Model):
    id_contact_type = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'contact_types'


class Contacts(models.Model):
    id_contact = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    faktura_address = models.TextField(blank=True, null=True)
    faktura_details = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    id_country = models.ForeignKey('Countries', models.DO_NOTHING, db_column='id_country', blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    addon = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    house_number = models.TextField(blank=True, null=True)
    statecode = models.TextField(blank=True, null=True)
    contact_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'
        ordering = ['id_contact']


class Countries(models.Model):
    id_country = models.CharField(primary_key=True, max_length=2)
    name = models.TextField()
    region = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Currencies(models.Model):
    short_name = models.TextField(primary_key=True)
    long_name = models.TextField(blank=True, null=True)
    exchange_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'currencies'


class CustomerGroups(models.Model):
    id_customer_group = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_groups'


class Customers(models.Model):
    id_customer = models.AutoField(primary_key=True)
    cust_ref_number = models.TextField()
    name = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    first_contact = models.DateTimeField(blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    last_sale = models.DateTimeField(blank=True, null=True)
    volume_of_sales = models.DecimalField(max_digits=17, decimal_places=4, blank=True, null=True)
    last_user = models.IntegerField(blank=True, null=True)
    last_change = models.DateTimeField(blank=True, null=True)
    vatid_nr = models.TextField(blank=True, null=True)
    calculate_vatid = models.NullBooleanField()
    calculate_dollar = models.NullBooleanField()
    id_customer_group = models.ForeignKey(CustomerGroups, models.DO_NOTHING, db_column='id_customer_group', blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    id_country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='id_country', blank=True, null=True)
    locked = models.BooleanField()
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'
        ordering = ['cust_ref_number']

    def __str__(self):
        if self.cust_ref_number:
            return self.cust_ref_number
        else:
            return str(self.id_customer)


class CustomersContacts(models.Model):
    id_customer_contact = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customers, models.DO_NOTHING, db_column='id_customer', blank=True, null=True)
    id_contact = models.ForeignKey(Contacts, models.DO_NOTHING, db_column='id_contact', blank=True, null=True)
    id_contact_type = models.ForeignKey(ContactTypes, models.DO_NOTHING, db_column='id_contact_type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers_contacts'
        unique_together = (('id_customer', 'id_contact'),)

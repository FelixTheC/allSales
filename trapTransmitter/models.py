from django.db import models
from django.urls import reverse
from ordercontact.models import Ordercontactinvoiceaddresse
from ordercontact.models import Ordercontactdeliveryaddresse


AREACHOICES = (
    ('', ''),
    ('Northern America', 'Northern America'),
    ('other', 'other part of the world'),
)


class Traptransmitterordermodel(models.Model):
    payment_option = models.CharField(max_length=255)
    order_no = models.CharField(max_length=255, blank=True, null=True)
    as_post = models.BooleanField(default=False)
    as_email = models.BooleanField(default=False)
    invoice_mail = models.CharField(max_length=254, blank=True, null=True)
    number_of_collars = models.CharField(max_length=100, blank=True, null=True)
    customer_faktura_id = models.IntegerField(blank=True, null=True)
    contacts_faktura_id = models.IntegerField(blank=True, null=True)
    same_addr = models.BooleanField(default=False)
    globalstar = models.BooleanField(default=False)
    iridium = models.BooleanField(default=False)
    vhf_beacon_schedule = models.CharField(max_length=255, blank=True, null=True)
    vhf_beacon_frequency = models.TextField(blank=True, null=True)
    contact_name_airtime_fee = models.CharField(max_length=255, blank=True, null=True)
    contact_mail_airtime_fee = models.CharField(max_length=254, blank=True, null=True)
    notification_mail = models.CharField(max_length=500, blank=True, null=True)
    notification_sms = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    customer_staff = models.CharField(max_length=255, blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    order_acceptet = models.BooleanField(default=False)
    operation_number = models.CharField(db_column='operation_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_tag = models.BooleanField(default=False)
    airtime_contract = models.CharField(max_length=100)
    vat_ein_number = models.CharField(max_length=255, blank=True, null=True)
    delivery_time = models.DateField(blank=True, null=True)
    inc_or_gmbh = models.CharField(max_length=13, blank=True, null=True)
    owm_gps_schedule = models.CharField(max_length=100, blank=True, null=True)
    own_vhf_schedule = models.CharField(max_length=100, blank=True, null=True)
    world_location = models.CharField(max_length=255, blank=True, null=True, choices=AREACHOICES)
    interval = models.IntegerField(blank=True, null=True)
    customer_invoice_address = models.ForeignKey(Ordercontactinvoiceaddresse, blank=True, null=True)
    delivery_addresse = models.ForeignKey(Ordercontactdeliveryaddresse, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trapTransmitterOrderModel'
        app_label = 'sales'

    def get_back_to_list(self):
        return reverse('sales:listsorders')

    def get_delete_url(self):
        return reverse('sales:traptransdelete', kwargs={'pk': self.pk})

    def get_sells_update_url(self):
        return reverse('sales:updatetraptrans', kwargs={'pk': self.pk})

    def get_sells_detail_url(self):
        return reverse('sales:detailtraptrans', kwargs={'pk': self.pk})

    def get_prod_rec(self):
        return reverse('sales:ttprodrec', kwargs={'pk': self.pk})

    def get_accept_url(self):
        return reverse('sales:accepttraptrans', kwargs={'pk': self.pk})

    def get_pdf(self):
        return reverse('sales:traptransorderpdf', kwargs={'pk': self.pk})

    def get_origin_pdf(self):
        return reverse('sales:traptransoriginpdf', kwargs={'pk': self.pk})

    def get_prod_rec_pdf(self):
        return reverse('sales:traptransprodrecpdf', kwargs={'pk': self.pk})

    def write_into_priolist(self):
        return reverse('sales:accepttraptranswriteprioliste', kwargs={'pk': self.pk})

    def get_model_type(self):
        return 'TT3'

    def get_co_worker(self):
        salesinput = SalesSalesinputtraptransmitter.objects.filter(order__pk=self.pk)
        try:
            return str(salesinput[0].co_worker)
        except IndexError:
            return ''

    def get_operation_number(self):
        return self.operation_number

    def check_for_prod_rec(self):
        prod_recs = SalesSalesinputtraptransmitter.objects.filter(order__pk=self.pk)
        if len(prod_recs) < 1:
            return False
        else:
            return True

    def __str__(self):
        return self.operation_number


class SalesSalesinputtraptransmitter(models.Model):
    co_worker = models.CharField(max_length=100, blank=True, null=True)
    further_instructions_programming = models.TextField(max_length=500, blank=True, null=True)
    path_customer_folder = models.CharField(max_length=500, blank=True, null=True)
    order = models.ForeignKey(Traptransmitterordermodel, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'sales'

    def __str__(self):
        return str(self.order.operation_number)

    def get_update_url(self):
        return reverse('sales:updateprodrectraptrans', kwargs={'pk': self.pk})
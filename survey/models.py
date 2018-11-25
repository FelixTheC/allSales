from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from ordercontact.models import Ordercontactinvoiceaddresse
from ordercontact.models import Ordercontactdeliveryaddresse
from sales.models import ProductionRecordInput


def upload_path(instance, filename):
    return '/'.join(['media', instance.contacts_faktura_id, filename])


class Surveyordermodel(models.Model):
    payment_option = models.CharField(max_length=255, blank=True, default='check')
    order_no = models.CharField(null=True, blank=True, max_length=255)
    as_post = models.BooleanField(default=False, blank=True)
    as_email = models.BooleanField(default=True, blank=True)
    invoice_mail = models.EmailField(null=True, blank=True)
    number_of_collars = models.CharField(null=True, blank=True, max_length=100)
    customer_faktura_id = models.IntegerField(editable=False, null=True)
    contacts_faktura_id = models.IntegerField(null=True, blank=True)
    customer_invoice_address = models.ForeignKey(Ordercontactinvoiceaddresse, null=True, blank=True)
    delivery_addresse = models.ForeignKey(Ordercontactdeliveryaddresse, null=True, blank=True)
    same_addr = models.BooleanField(blank=True, default=True)
    animal_species = models.CharField(max_length=255, blank=True, null=True)
    battery_size = models.CharField(max_length=100, null=True, blank=True)
    belt_shape = models.CharField(max_length=255, blank=True, null=True)
    nom_collar_circumference = models.TextField(blank=True, null=True, max_length=255)
    vhf_beacon_frequency = models.TextField(blank=True, null=True, default=148)
    mortality_sensor = models.PositiveIntegerField(blank=True, null=True, default=24)
    external_dropoff = models.BooleanField(blank=True, default=False)
    external_dropoff_controll = models.CharField(blank=True, null=True, max_length=200)
    external_dropoff_real_time = models.CharField(blank=True, null=True, max_length=200)
    external_dropoff_abs_time = models.CharField(blank=True, null=True, max_length=200)
    utc_lmt = models.CharField(blank=True, default=False, max_length=50, null=True)
    utc_correction = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    vhf_beacon_schedule = models.CharField(blank=True, default='24', max_length=255, null=True)
    globalstar = models.BooleanField(blank=True, default=False)
    iridium = models.BooleanField(blank=True, default=False)
    gps_schedule = models.CharField(blank=True, default='Every 13h', max_length=255,  null=True)
    iridium_contract_type = models.CharField(max_length=255, blank=True, null=True)
    iridium_num_of_fixes_gps = models.IntegerField(blank=True, null=True)
    contact_name_airtime_fee = models.CharField(blank=True, null=True, max_length=255)
    contact_mail_airtime_fee = models.EmailField(blank=True, null=True)
    notification_mail = models.CharField(blank=True, null=True, max_length=500)
    notification_sms = models.CharField(blank=True, null=True, max_length=255)
    belt_width = models.CharField(blank=True, null=True, max_length=255)
    belt_thickness = models.CharField(blank=True, null=True, max_length=255)
    belt_edge = models.CharField(blank=True, null=True, max_length=255, default='round')
    belt_colour = models.CharField(blank=True, null=True, max_length=255)
    other_color = models.CharField(max_length=100, blank=True, null=True)
    belt_labeling = models.BooleanField(blank=True, default=False)
    belt_labeling_instructions = models.CharField(max_length=255, null=True, blank=True)
    belt_plates = models.BooleanField(blank=True, default=False)
    belt_plates_instructions = models.CharField(max_length=76, null=True, blank=True)

    reflective_stripes = models.BooleanField(blank=True, default=False)
    reflective_stripes_instructions = models.CharField(max_length=76, null=True, blank=True)

    cotton_layers = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    customer_staff = models.CharField(blank=True, null=True, max_length=255)
    origin = models.TextField(editable=False, null=True, blank=True, max_length=1000)
    order_acceptet = models.BooleanField(default=False)
    operation_Number = models.CharField(max_length=255, blank=True, null=True)
    id_tag = models.BooleanField(blank=True, default=False)
    airtime_contract = models.CharField(max_length=200, blank=True, null=True)
    vat_ein_number = models.CharField(max_length=255, blank=True, null=True, default='')
    delivery_time = models.DateField(blank=True, null=True)
    inc_or_gmbh = models.CharField(blank=True, null=True, default='gmbh', max_length=10)
    owm_gps_schedule = models.CharField(max_length=100, blank=True, null=True)
    own_vhf_schedule = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SurveyOrderModel'
        app_label = 'sales'

    def get_back_to_list(self):
        return reverse('sales:listsorders')

    def get_delete_url(self):
        return reverse('sales:surveydelete', kwargs={'pk': self.pk})

    def get_sells_update_url(self):
        return reverse('sales:updatesurveys', kwargs={'pk': self.pk})

    def get_sells_detail_url(self):
        return reverse('sales:detailsurveys', kwargs={'pk': self.pk})

    def get_accept_url(self):
        return reverse('sales:acceptsurvey', kwargs={'pk': self.pk})

    def get_prod_rec(self):
        return reverse('sales:prodrec', kwargs={'pk': self.pk})

    def get_pdf(self):
        return reverse('sales:surveyorderpdf', kwargs={'pk': self.pk})

    def get_origin_pdf(self):
        return reverse('sales:surveyoriginpdf', kwargs={'pk': self.pk})

    def get_prod_rec_pdf(self):
        return reverse('sales:prodrecpdf', kwargs={'pk': self.pk})

    def write_into_priolist(self):
        return reverse('sales:acceptsurveywriteprioliste', kwargs={'pk': self.pk})

    def get_model_type(self):
        return 'Survey'

    def get_co_worker(self):
        salesinput = SalesSalesinputsurvey.objects.filter(order__pk=self.pk)
        try:
            return str(salesinput[0].co_worker)
        except IndexError:
            return ''

    def get_operation_number(self):
        return self.operation_Number

    def check_for_prod_rec(self):
        prod_recs = SalesSalesinputsurvey.objects.filter(order__pk=self.pk)
        if len(prod_recs) < 1:
            return False
        else:
            return True

    def __str__(self):
        return self.operation_Number


class SalesSalesinputsurvey(ProductionRecordInput):
    order = models.ForeignKey(Surveyordermodel, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sales_salesinputsurvey'
        app_label = 'sales'

    def __str__(self):
        try:
            return str(self.order.operation_Number)
        except AttributeError:
            return str(self.order.operation_number)

    def get_update_url(self):
        return reverse('sales:updateprodrec', kwargs={'pk': self.pk})


class SurveyProdRec(models.Model):
    order = models.ForeignKey(Surveyordermodel)
    salesinput = models.ManyToManyField(SalesSalesinputsurvey)

    class Meta:
        app_label = 'sales'
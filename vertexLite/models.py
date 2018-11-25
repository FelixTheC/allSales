from django.db import models
from django.urls import reverse
from ordercontact.models import Ordercontactinvoiceaddresse
from ordercontact.models import Ordercontactdeliveryaddresse
from sales.models import ProductionRecordInput
from sales.models import BaseModel

VERTEXLITEBELTSHAPES = (
    ('round-shaped', 'round-shaped'),
    ('drop-shaped', 'drop-shaped'),
    ('ovalround-shaped', 'ovalround-shaped')
)


def upload_path(instance, filename):
    return '/'.join(['media', instance.contacts_faktura_id, filename])


class Vertexliteordermodel(BaseModel):

    belt_shape = models.CharField(max_length=255, blank=True, null=True, choices=VERTEXLITEBELTSHAPES)
    reflective_stripes = models.BooleanField(default=False)
    reflective_stripes_instructions = models.CharField(max_length=76, blank=True, null=True)
    external_dropoff = models.BooleanField(default=False)
    external_dropoff_controll = models.CharField(max_length=200, blank=True, null=True)
    external_dropoff_real_time = models.CharField(max_length=200, blank=True, null=True)
    external_dropoff_abs_time = models.CharField(max_length=200, blank=True, null=True)
    internal_dropoff = models.BooleanField(default=False)
    internal_dropoff_controll = models.CharField(max_length=200, blank=True, null=True)
    internal_dropoff_real_time = models.CharField(max_length=200, blank=True, null=True)
    internal_dropoff_abs_time = models.CharField(max_length=200, blank=True, null=True)
    store_on_board = models.BooleanField(default=False)
    gsm = models.BooleanField(default=False)
    gsm_vectronic_sim = models.BooleanField(default=False)
    gsm_mode = models.CharField(max_length=1, blank=True, null=True)
    gsm_customer_sim_telephone_no = models.CharField(max_length=9999, blank=True, null=True)
    gsm_customer_sim_pin = models.CharField(max_length=9999, blank=True, null=True)
    gsm_customer_sim_puk = models.CharField(max_length=9999, blank=True, null=True)
    groundstation_number = models.CharField(null=True, blank=True, max_length=255)
    customer_invoice_address = models.ForeignKey(Ordercontactinvoiceaddresse, blank=True, null=True)
    delivery_addresse = models.ForeignKey(Ordercontactdeliveryaddresse, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VertexLiteOrderModel'
        app_label = 'sales'

    def get_back_to_list(self):
        return reverse('sales:listsorders')

    def get_delete_url(self):
        return reverse('sales:vertexlitedelete', kwargs={'pk': self.pk})

    def get_sells_update_url(self):
        return reverse('sales:updatevertexlite', kwargs={'pk': self.pk})

    def get_sells_detail_url(self):
        return reverse('sales:detailvertexlite', kwargs={'pk': self.pk})

    def get_prod_rec(self):
        return reverse('sales:vlprodrec', kwargs={'pk': self.pk})

    def get_accept_url(self):
        return reverse('sales:acceptvertexlite', kwargs={'pk': self.pk})

    def get_pdf(self):
        return reverse('sales:vertexliteorderpdf', kwargs={'pk': self.pk})

    def get_origin_pdf(self):
        return reverse('sales:vertexliteoriginpdf', kwargs={'pk': self.pk})

    def get_prod_rec_pdf(self):
        return reverse('sales:vtxlprodrecpdf', kwargs={'pk': self.pk})

    def write_into_priolist(self):
        return reverse('sales:acceptvertexlitewriteprioliste', kwargs={'pk': self.pk})

    def get_model_type(self):
        return 'Vertex Lite'

    def get_co_worker(self):
        salesinput = SalesSalesinputvertexlite.objects.filter(order__pk=self.pk)
        try:
            return str(salesinput[0].co_worker)
        except IndexError:
            return ''

    def get_operation_number(self):
        return self.operation_number

    def check_for_prod_rec(self):
        prod_recs = SalesSalesinputvertexlite.objects.filter(order__pk=self.pk)
        if len(prod_recs) < 1:
            return False
        else:
            return True

    def __str__(self):
        return self.operation_number


class SalesSalesinputvertexlite(ProductionRecordInput):
    protective_belt = models.BooleanField(default=False)
    order = models.ForeignKey(Vertexliteordermodel, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'sales'

    def __str__(self):
        return str(self.order.operation_number)

    def get_update_url(self):
        return reverse('sales:updateprodrecvtxl', kwargs={'pk': self.pk})

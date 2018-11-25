from django.db import models
from django.urls import reverse
from ordercontact.models import Ordercontactinvoiceaddresse
from ordercontact.models import Ordercontactdeliveryaddresse
from sales.models import ProductionRecordInputMiniGL

from sales.models import BaseModelWithoutBeltDesign


class Minifawnordermodel(BaseModelWithoutBeltDesign):
    min_belt_circumference = models.CharField(null=True, blank=True, max_length=100)
    max_belt_circumference = models.CharField(null=True, blank=True, max_length=100)
    skip_count = models.CharField(null=True, blank=True, max_length=255)
    customer_invoice_address = models.ForeignKey(Ordercontactinvoiceaddresse, blank=True, null=True)
    delivery_addresse = models.ForeignKey(Ordercontactdeliveryaddresse, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'miniFawnOrderModel'
        app_label = 'sales'

    def get_back_to_list(self):
        return reverse('sales:listsorders')

    def get_delete_url(self):
        return reverse('sales:minifawndelete', kwargs={'pk': self.pk})

    def get_sells_update_url(self):
        return reverse('sales:updateminifawn', kwargs={'pk': self.pk})

    def get_sells_detail_url(self):
        return reverse('sales:detailminifawn', kwargs={'pk': self.pk})

    def get_prod_rec(self):
        return reverse('sales:mfprodrec', kwargs={'pk': self.pk})

    def get_accept_url(self):
        return reverse('sales:acceptminifawn', kwargs={'pk': self.pk})

    def get_pdf(self):
        return reverse('sales:minifawnorderpdf', kwargs={'pk': self.pk})

    def get_origin_pdf(self):
        return reverse('sales:minifawnoriginpdf', kwargs={'pk': self.pk})

    def get_prod_rec_pdf(self):
        return reverse('sales:mfprodrecpdf', kwargs={'pk': self.pk})

    def write_into_priolist(self):
        return reverse('sales:acceptminifawnwriteprioliste', kwargs={'pk': self.pk})

    def get_model_type(self):
        return 'Mini Fawn'

    def get_co_worker(self):
        salesinput = SalesSalesinputminifawn.objects.filter(order__pk=self.pk)
        try:
            return str(salesinput[0].co_worker)
        except IndexError:
            return ''

    def get_operation_number(self):
        return self.operation_number

    def check_for_prod_rec(self):
        prod_recs = SalesSalesinputminifawn.objects.filter(order__pk=self.pk)
        if len(prod_recs) < 1:
            return False
        else:
            return True

    def __str__(self):
        return self.operation_number


class SalesSalesinputminifawn(ProductionRecordInputMiniGL):
    order = models.ForeignKey(Minifawnordermodel, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'sales'

    def __str__(self):
        return str(self.order.operation_number)

    def get_update_url(self):
        return reverse('sales:updateprodrecmf', kwargs={'pk': self.pk})
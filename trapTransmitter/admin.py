from django.contrib import admin
from sales.utils import ADMINLISTDISPLAY
from .models import Traptransmitterordermodel
from .models import SalesSalesinputtraptransmitter


class TrapTransmitterAdmin(admin.ModelAdmin):
    list_display = ADMINLISTDISPLAY


class SalesSalesinputtraptransAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'order_id',
    )


admin.site.register(Traptransmitterordermodel, TrapTransmitterAdmin)
admin.site.register(SalesSalesinputtraptransmitter, SalesSalesinputtraptransAdmin)
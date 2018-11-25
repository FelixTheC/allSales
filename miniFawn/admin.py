from django.contrib import admin
from sales.utils import ADMINLISTDISPLAY
from .models import Minifawnordermodel
from .models import SalesSalesinputminifawn


class MiniFawnAdmin(admin.ModelAdmin):
    list_display = ADMINLISTDISPLAY


class SalesSalesinputminifawnAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'order_id',
    )


admin.site.register(Minifawnordermodel, MiniFawnAdmin)
admin.site.register(SalesSalesinputminifawn, SalesSalesinputminifawnAdmin)
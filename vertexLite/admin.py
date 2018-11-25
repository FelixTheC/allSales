from django.contrib import admin

from django.contrib import admin

from sales.utils import ADMINLISTDISPLAY
from .models import Vertexliteordermodel
from .models import SalesSalesinputvertexlite


class VertexLiteAdmin(admin.ModelAdmin):
    list_display = ADMINLISTDISPLAY + ('pk', )


class SalesSalesinputvertexliteAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'order_id',
    )


admin.site.register(Vertexliteordermodel, VertexLiteAdmin)
admin.site.register(SalesSalesinputvertexlite, SalesSalesinputvertexliteAdmin)

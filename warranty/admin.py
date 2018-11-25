from django.contrib import admin
from .models import Warranty


class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'comment', 'description_failure')


admin.site.register(Warranty, WarrantyAdmin)

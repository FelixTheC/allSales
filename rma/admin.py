from django.contrib import admin
from .models import Status
from .models import Refurbisment


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


class RefurbishmentAdmin(admin.ModelAdmin):
    list_display = ('rma', 'salesPerson', 'status')


admin.site.register(Status, StatusAdmin)
admin.site.register(Refurbisment, RefurbishmentAdmin)

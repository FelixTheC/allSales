from django.contrib import admin

# Register your models here.
from .models import PriolisteAssignment
from .models import Shelf
from .models import StaffColor
from .models import ProductionTime


def reset_box_number(modeladmin, request, queryset):
    queryset.update(box=None)


reset_box_number.short_description = 'Reset box from selected Assignment'


class PrioListeAdmin(admin.ModelAdmin):
    list_display = ['internal_progress_number',
                    'ordering_number',
                    'box',
                    'finished_until',
                    'staff',
                    'status',
                    'customer',
                    'hardware',
                    'last_change',
                    'changed_by_ip', ]
    list_display_links = ['internal_progress_number',
                          'ordering_number',
                          'box',
                          'finished_until',]
    list_filter = ['status',
                   'staff',
                   'customer',
                   'box']

    actions = [reset_box_number, ]


class ShelfAdmin(admin.ModelAdmin):
    list_display = ['shelf_type',
                    'compartment',
                    'assignment']


class StaffColorAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'color']


class ProductionTimeAdmin(admin.ModelAdmin):
    list_display = ['time_in_weeks',
                    'enabled']


admin.site.register(PriolisteAssignment, PrioListeAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(StaffColor, StaffColorAdmin)
admin.site.register(ProductionTime, ProductionTimeAdmin)
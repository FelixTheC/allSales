from django.contrib import admin
from .models import Surveyordermodel
from .models import SalesSalesinputsurvey
from .models import SurveyProdRec


# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
    list_display = (
        'operation_Number', 'pk', 'number_of_collars', 'delivery_addresse', 'origin', 'contacts_faktura_id'
    )


class SalesInputAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'animal_species', 'order'
    )


class SurveyProdRecAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'order_id',
    )


admin.site.register(Surveyordermodel, SurveyAdmin)
admin.site.register(SalesSalesinputsurvey, SalesInputAdmin)
admin.site.register(SurveyProdRec, SurveyProdRecAdmin)

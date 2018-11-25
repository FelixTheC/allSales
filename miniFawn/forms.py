from django import forms
from .models import Minifawnordermodel
from .models import SalesSalesinputminifawn
from sales.utils import PRODRECWIDGETS, MINIPRODWIDGETS
from survey.forms import ProdRecCreateForm


class MiniFawnUpdateForm(forms.ModelForm):
    class Meta:
        model = Minifawnordermodel
        fields = ('animal_species', 'battery_size', 'number_of_collars', 'min_belt_circumference',
                  'max_belt_circumference', 'vhf_beacon_frequency', 'mortality_sensor', 'notification_mail',
                  'notification_sms', 'utc_lmt', 'utc_correction', 'gps_schedule', 'vhf_beacon_schedule', 'skip_count',
                  'id_tag', 'globalstar', 'iridium', 'contact_name_airtime_fee',
                  'contact_mail_airtime_fee', 'cotton_layers', 'comment', 'delivery_time', 'payment_option',
                  'operation_number')


class MiniFawnProdRecForm(ProdRecCreateForm):
    class Meta:
        model = SalesSalesinputminifawn
        fields = ('co_worker',
                  'animal_species',
                  'gps_schedule_name',
                  'vhf_schedule_name',
                  'gl_no_of_attempts',
                  'gl_fixes_per_message',
                  'further_instructions_programming',
                  'path_customer_folder',
                  'order')

        widgets = PRODRECWIDGETS


class SalesInputMiniFawnCreateForm(forms.ModelForm):
    class Meta:
        model = SalesSalesinputminifawn
        # exclude = ('order',)
        fields = ('further_instructions_programming',)

        widgets = MINIPRODWIDGETS

        labels = {
            'gl_no_of_attempts': 'GLOBALSTAR no of attempts',
            'gl_fixes_per_message': 'GLOBALSTAR fixes per message',
        }
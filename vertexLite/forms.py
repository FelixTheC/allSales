from django import forms
from sales.utils import PRODRECWIDGETS
from sales.utils import MINIPRODWIDGETS
from .models import Vertexliteordermodel
from .models import SalesSalesinputvertexlite
from survey.forms import ProdRecCreateForm


class VertexLiteUpdateForm(forms.ModelForm):
    class Meta:
        model = Vertexliteordermodel
        fields = ('animal_species', 'battery_size', 'number_of_collars',
                  'nom_collar_circumference', 'belt_shape', 'belt_width',
                  'belt_thickness', 'belt_edge', 'belt_colour', 'other_color', 'belt_labeling',
                  'belt_labeling_instructions',
                  'belt_plates', 'belt_plates_instructions', 'reflective_stripes',
                  'vhf_beacon_frequency', 'mortality_sensor', 'notification_mail', 'notification_sms', 'utc_lmt',
                  'utc_correction', 'gps_schedule', 'vhf_beacon_schedule', 'id_tag', 'globalstar', 'store_on_board',
                  'iridium', 'gsm', 'gsm_vectronic_sim', 'groundstation_number', 'iridium_num_of_fixes_gps', 'iridium_contract_type',
                  'contact_name_airtime_fee', 'contact_mail_airtime_fee', 'gsm_mode', 'gsm_customer_sim_telephone_no',
                  'gsm_customer_sim_pin', 'gsm_customer_sim_puk', 'external_dropoff', 'external_dropoff_controll',
                  'external_dropoff_real_time', 'external_dropoff_abs_time', 'internal_dropoff',
                  'internal_dropoff_controll', 'internal_dropoff_real_time', 'cotton_layers',
                  'comment', 'delivery_time', 'payment_option', 'operation_number')


class VertexLiteProdRecForm(ProdRecCreateForm):
    class Meta:
        model = SalesSalesinputvertexlite
        fields = ('co_worker',
                  'animal_species',
                  'punching1_dist',
                  'punching1_pos',
                  'punching1_neg',
                  'punching2',
                  'protective_belt',
                  'further_instructions_belt',
                  'gps_schedule_name',
                  'vhf_schedule_name',
                  'gl_no_of_attempts',
                  'gl_fixes_per_message',
                  'ir_contract_type',
                  'ir_fixes_per_message',
                  'further_instructions_programming',
                  'path_customer_folder',
                  'order')
        vtxLiteWidgets = PRODRECWIDGETS
        vtxLiteWidgets['protective_belt'] = forms.CheckboxInput(attrs={
            'class': 'sales-input',
        })
        widgets = vtxLiteWidgets


class SalesInputVertexLiteCreateForm(forms.ModelForm):
    class Meta:
        model = SalesSalesinputvertexlite
        # exclude = ('order',)
        fields = ('punching1_dist',
                  'punching1_pos',
                  'punching1_neg',
                  'punching2',
                  'protective_belt',
                  'further_instructions_belt',)

        vtxLiteWidgets = MINIPRODWIDGETS
        vtxLiteWidgets['protective_belt'] = forms.CheckboxInput(attrs={
            'class': 'sales-input',
        })
        widgets = vtxLiteWidgets

        labels = {
            'gl_no_of_attempts': 'GLOBALSTAR no of attempts',
            'gl_fixes_per_message': 'GLOBALSTAR fixes per message',
            'ir_fixes_per_message': 'IRIDIUM fixes per message',
        }
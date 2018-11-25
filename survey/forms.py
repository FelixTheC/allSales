from django import forms
from sales.utils import IRIDIUM_CONTRACT_TYPES
from sales.utils import MINIPRODWIDGETS
from sales.utils import PRODRECWIDGETS
from .models import Surveyordermodel
from .models import SalesSalesinputsurvey


class SurveyUpdateForm(forms.ModelForm):
    class Meta:
        model = Surveyordermodel
        fields = ('animal_species', 'battery_size', 'number_of_collars',
                  'nom_collar_circumference', 'belt_shape', 'belt_width',
                  'belt_thickness', 'belt_edge', 'belt_colour', 'other_color', 'belt_labeling',
                  'belt_labeling_instructions',
                  'belt_plates', 'belt_plates_instructions', 'reflective_stripes',
                  'vhf_beacon_frequency', 'mortality_sensor', 'notification_mail', 'notification_sms', 'utc_lmt',
                  'utc_correction', 'gps_schedule', 'vhf_beacon_schedule', 'id_tag', 'globalstar', 'iridium',
                  'iridium_num_of_fixes_gps', 'iridium_contract_type', 'contact_name_airtime_fee', 'contact_mail_airtime_fee',
                  'external_dropoff', 'external_dropoff_controll', 'external_dropoff_real_time',
                  'external_dropoff_abs_time', 'cotton_layers', 'comment', 'delivery_time',
                  'payment_option', 'operation_Number')

        widgets = {
            'vhf_beacon_frequency': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
            'belt_labeling_instructions': forms.Textarea(attrs={'rows': 4, 'cols': 20, 'style': 'resize:none;',
                                                                'maxlength': 76}),
            'belt_plates_instructions': forms.Textarea(attrs={'rows': 2, 'cols': 20, 'maxlength': 76}),
            'utc_correction': forms.NumberInput(attrs={
                'min': '-13.00', 'max': '13:00', 'step': '0.05',
            }),
            'mortality_sensor': forms.NumberInput(attrs={
                'min': '0', 'max': '140', 'step': '1',
            }),
            'nom_collar_circumference': forms.TextInput(),
            'iridium_num_of_fixes_gps': forms.NumberInput(attrs={
                'min': '0', 'max': '18', 'step': '1',
            }),
            'belt_labeling': forms.CheckboxInput(attrs={
                'class': 'lable_plates', 'onclick': 'lable_function()',
            }),
            'belt_plates': forms.CheckboxInput(attrs={
                'class': 'lable_plates', 'onclick': 'plates_function()',
            }),
            'cotton_layers': forms.NumberInput(attrs={
                'min': '0', 'max': '6', 'step': '1',
            }),
            'iridium_contract_type': forms.Select(choices=IRIDIUM_CONTRACT_TYPES)
        }
        labels = {
            'order_acceptet': 'Accept Order',
            'belt_colour': 'Belt color',
            'belt_labeling': 'Label plates',
            'belt_labeling_instructions': 'Label plates instructions',
            'belt_plates': 'Belt marking',
            'belt_plates_instructions': 'Belt marking instructions',
            'vhf_beacon_frequency': 'VHF beacon frequency',
            'notification_mail': 'Notification email',
            'notification_sms': 'Notification SMS',
            'utc_lmt': 'UTC/LMT',
            'gps_schedule': 'GPS schedule',
            'vhf_beacon_schedule': 'VHF beacon schedule',
            'id_tag': 'ID-Tag',
            'external_dropoff': 'External Drop Off',
            'external_dropoff_controll': 'External Drop Off controll',
            'external_dropoff_real_time': 'External Drop Off realative release time',
            'external_dropoff_abs_time': 'External Drop Off absolute release time',
            'delivery_addresse': 'Delivery address',
        }


class SalesInputSurveyCreateForm(forms.ModelForm):
    class Meta:
        model = SalesSalesinputsurvey
        # exclude = ('order',)
        fields = ('punching1_dist',
                  'punching1_pos',
                  'punching1_neg',
                  'punching2',
                  'further_instructions_belt',)

        widgets = MINIPRODWIDGETS

        labels = {
            'gl_no_of_attempts': 'GLOBALSTAR no of attempts',
            'gl_fixes_per_message': 'GLOBALSTAR fixes per message',
            'ir_fixes_per_message': 'IRIDIUM fixes per message',
        }


class ProdRecCreateForm(forms.ModelForm):
    class Meta:
        model = SalesSalesinputsurvey
        fields = ('co_worker',
                  'animal_species',
                  'punching1_dist',
                  'punching1_pos',
                  'punching1_neg',
                  'punching2',
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

        widgets = PRODRECWIDGETS
        labels = {
            'gl_no_of_attempts': 'GLOBALSTAR no of attempts',
            'gl_fixes_per_message': 'GLOBALSTAR fixes per message',
            'ir_fixes_per_message': 'IRIDIUM fixes per message',
            'animal_species': 'Animal species',
        }

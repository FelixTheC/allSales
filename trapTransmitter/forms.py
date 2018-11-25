from django import forms
from sales.utils import PRODRECWIDGETS, MINIPRODWIDGETS
from survey.forms import ProdRecCreateForm
from trapTransmitter.models import Traptransmitterordermodel, SalesSalesinputtraptransmitter


class TrapTransmitterUpdateForm(forms.ModelForm):
    class Meta:
        model = Traptransmitterordermodel
        fields = ('number_of_collars',
                  'vhf_beacon_frequency', 'notification_mail', 'notification_sms',
                  'vhf_beacon_schedule', 'id_tag', 'globalstar', 'iridium', 'contact_name_airtime_fee',
                  'contact_mail_airtime_fee', 'world_location', 'interval', 'comment', 'delivery_time',
                  'payment_option', 'operation_number')


class TrapTransmitterProdRecForm(ProdRecCreateForm):
    class Meta:
        model = SalesSalesinputtraptransmitter
        fields = ('co_worker',
                  'further_instructions_programming',
                  'path_customer_folder',
                  'order')

        widgets = PRODRECWIDGETS


class SalesInputTrapTransCreateForm(forms.ModelForm):
    class Meta:
        model = SalesSalesinputtraptransmitter
        # exclude = ('order',)
        fields = ('further_instructions_programming',)

        widgets = MINIPRODWIDGETS

        labels = {
            'gl_no_of_attempts': 'GLOBALSTAR no of attempts',
            'gl_fixes_per_message': 'GLOBALSTAR fixes per message',
        }
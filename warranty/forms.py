from datetime import datetime

from django import forms

from .models import Warranty


class CustomerForm(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


class WarrantyForm(forms.ModelForm):
    class Meta:
        model = Warranty
        exclude = ('date_complaint', 'deleted')
        help_texts = {
            'customer_collar': 'Please hold down ctrl/strg or for Mac command to select multiple entries',
        }
        widgets = {
            'customer_collar': forms.SelectMultiple(attrs={'class': 'radio1',
                                                        'size': 20, 'required': False}),
        }
        help_texts = {
            'date_delivery': 'Use yyyy-mm-dd as date format',
            'date_collar_failure': 'Use yyyy-mm-dd as date format',
        }

    def clean(self):
        pass
        # cleaned_data = super(WarrantyForm, self).clean()
        # date_delivery = cleaned_data.get('date_delivery')
        # date_of_failure = cleaned_data.get('date_collar_failure')
        # try:
        #     datetime.strptime(date_delivery, '%d.%m.%Y')
        # except ValueError:
        #     self.add_error('date_delivery', 'Please use dd.mm.yyyy as date format')
        # try:
        #     datetime.strptime(date_of_failure, '%d.%m.%Y')
        # except ValueError:
        #     self.add_error('date_collar_failure', 'Please use dd.mm.yyyy as date format')


class WarrantyUpdateForm(forms.ModelForm):
    class Meta:
        model = Warranty
        exclude = ('date', 'contact_person', 'custom_collar', 'deleted')
        help_texts = {
            'customer_collar': 'Please hold down ctrl/strg or for Mac command to select multiple entries',
        }
        widgets = {
            'customer_collar': forms.SelectMultiple(attrs={'class': 'radio1',
                                                           'size': 20, 'required': False}),
        }
        help_texts = {
            'date_delivery': 'Use dd.mm.yyyy as date format',
            'date_collar_failure': 'Use dd.mm.yyyy as date format',
        }

    def clean(self):
        pass
        # cleaned_data = super(WarrantyUpdateForm, self).clean()
        # date_delivery = cleaned_data.get('date_delivery')
        # date_of_failure = cleaned_data.get('date_collar_failure')
        # try:
        #     datetime.strptime(date_delivery, '%d.%m.%Y')
        # except ValueError:
        #     self.add_error('date_delivery', 'Please use dd.mm.yyyy as date format')
        # try:
        #     datetime.strptime(date_of_failure, '%d.%m.%Y')
        # except ValueError:
        #     self.add_error('date_collar_failure', 'Please use dd.mm.yyyy as date format')
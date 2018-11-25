from django import forms
from django.forms import Textarea

from .models import Refurbisment
from django.utils.timezone import now

class RefursbishmentForm(forms.ModelForm):
    class Meta:
        model = Refurbisment
        fields = '__all__'
        widgets = {
            'rma': Textarea(attrs={'cols': 20, 'rows': 2}),
            'customer_forename': Textarea(attrs={'cols': 20, 'rows': 2}),
            'customer_name': Textarea(attrs={'cols': 20, 'rows': 2}),
            'country': Textarea(attrs={'cols': 20, 'rows': 2}),
            'content': Textarea(attrs={'cols': 30, 'rows': 10}),
            'comments': Textarea(attrs={'cols': 30, 'rows': 10}),
            'rma_file': forms.ClearableFileInput(attrs={'multiple': True}),
            'shelf': forms.NumberInput(attrs={'min': '0', 'max': '30', 'step': '1'})
        }


class RefursbishmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Refurbisment
        fields = '__all__'
        widgets = {
            'rma': Textarea(attrs={'cols': 20, 'rows': 2}),
            'customer_forename': Textarea(attrs={'cols': 20, 'rows': 2}),
            'customer_name': Textarea(attrs={'cols': 20, 'rows': 2}),
            'country': Textarea(attrs={'cols': 20, 'rows': 2}),
            'content': Textarea(attrs={'cols': 30, 'rows': 10}),
            'comments': Textarea(attrs={'cols': 30, 'rows': 10}),
            'rma_file': forms.ClearableFileInput(attrs={'multiple': True}),
            'more_files': forms.Textarea(attrs={'cols': 20, 'rows': 2, 'readonly': 'readonly'}),
            'shelf': forms.NumberInput(attrs={'min': '0', 'max': '30', 'step': '1'})
        }


class RMASearchForm(forms.Form):
    search = forms.CharField(label='Search', required=False)
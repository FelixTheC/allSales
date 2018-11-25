from collar.models import Staff
from django import forms
from django.forms import ComboField
from faktura.models import Customers

COLLARCHOICE = (
    ('Survey', 'Survey'),
    ('VertexLite', 'VertexLite'),
    ('MiniFawn', 'MiniFawn'),
    ('TrapTransmitter', 'TrapTransmitter'),
)

COMMUNICATION_CHOICE = (
    ('GL', 'Globalstar'),
    ('IR', 'IRIDIUM'),
    ('GSM', 'GSM'),
    ('SOB', 'SOB'),
)

COMPANY_CHOICE = (
    ('gmbh', 'VASGmbH'),
    ('inc', 'VASInc'),
)


class LinkCreateForm(forms.Form):
    staff = forms.ModelChoiceField(queryset=Staff.objects.all())
    contact_person = forms.ModelChoiceField(queryset=Customers.objects.all(), label='Customer number')
    customerEmail = forms.EmailField(label='Customer e-mail')
    operation_Number = forms.CharField(label='Faktura process number')
    collarType = forms.ChoiceField(choices=COLLARCHOICE, label='Faktura type')
    communicationType = forms.ChoiceField(choices=COMMUNICATION_CHOICE, label='Communication type')
    company = forms.ChoiceField(choices=COMPANY_CHOICE)

    def clean(self):
        cleaned_data = super(LinkCreateForm, self).clean()
        collarType = cleaned_data.get('collarType')
        communicationType = cleaned_data.get('communicationType')

        if collarType is not None:
            if collarType == 'Survey' or collarType == 'TrapTransmitter':
                if communicationType == 'GSM':
                    self.add_error('communicationType', 'Survey has no GSM communication')
            elif collarType == 'MiniFawn':
                if communicationType != 'GL':
                    self.add_error('communicationType', 'MiniFawn has only GLOBALSTAR communication')


class StaffChoiceForm(forms.Form):
    staff = forms.ModelChoiceField(queryset=Staff.objects.all())


class SearchForm(forms.Form):
    search_string = forms.CharField(required=False, label='Search')
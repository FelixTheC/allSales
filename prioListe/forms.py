from datetime import datetime
from django import forms
from django.forms import BaseFormSet
from django.utils.translation import ugettext as _
import re
from prioListe.utils import update_time_in_weeks

from prioListe.utils import STAFFCHOICESONE, STAFFCHOICESTWO
from .models import PriolisteAssignment


class CreateForm(forms.ModelForm):
    class Meta:
        model = PriolisteAssignment
        fields = ['staff', 'co_worker', 'box', 'ordering_number',
                  'customer', 'hardware']

        labels = {
            'box': _('Kiste: '),
            'customer': _('Kunde: '),
            'hardware': _('Hardware: '),
            'status': _('Status: '),
            'optional_status': _('Status: '),
            'staff': _('erstellt von Mitarbeiter: '),
            'production_remark': _('Produktionsbemerkung: '),
        }
        widgets = {
            'box': forms.NumberInput(attrs={
                'min': '1', 'max': '999', 'step': '1'
            }),
            'staff': forms.Select(choices=STAFFCHOICESONE),
            'co_worker': forms.Select(choices=STAFFCHOICESTWO),
            'last_change': forms.TextInput(attrs={'readonly': 'readonly'}),
            'created_at': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        help_texts = {
            'box': 'Only for Refurbishments',
        }
    # created_at = forms.DateField(label=_('Erstellt am: '),
    #                              required=False,
    #                              initial=datetime.today(),
    #                              )
    # finished_until = forms.DateField(label=_('Fertig bis: '),
    #                                  required=False,
    #                                  initial=datetime.today())
    # time_in_weeks = forms.IntegerField(label=_('Zeit in Wochen: '),
    #                                    required=False,
    #                                    initial=12)


class CreateFormFromOrder(forms.ModelForm):
    class Meta:
        model = PriolisteAssignment
        fields = ('box', 'remark',)


class UpdateSelectForm(forms.ModelForm):
    class Meta:
        model = PriolisteAssignment
        fields = ['status', 'optional_status', 'staff', 'co_worker', 'ordering_number', 'box', 'customer', 'hardware',
                  'production_remark', 'ids', 'remark', 'last_change', 'created_at',
                  'prod_rec_one', 'prod_rec_two', 'prod_rec_three', 'prod_rec_four', 'prod_rec_five', 'changed_by_ip']
        labels = {
            'box': _('Kiste: '),
            'customer': _('Kunde: '),
            'hardware': _('Hardware: '),
            'created_at': _('Erstellt am: '),
            'status': _('Status: '),
            'optional_status': _('Status: '),
            'finished_until': _('Fertig bis: '),
            'staff': _('erstellt von Mitarbeiter: '),
            'time_in_weeks': _('Zeit in Wochen: '),
            'production_remark': 'Production remark - for production ONLY',
            'remark': 'Sales remark - for sales ONLY',
        }
        widgets = {
            'hardware': forms.Textarea(attrs={'readonly': 'readonly', 'col': 1, 'rows': 1}),
            'last_change': forms.TextInput(attrs={'readonly': 'readonly'}),
            'staff': forms.Select(choices=STAFFCHOICESONE),
            'co_worker': forms.Select(choices=STAFFCHOICESTWO),
            'created_at': forms.TextInput(attrs={'readonly': 'readonly'}),
            'customer': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    #config_file = forms.FileField(required=False)
    id_file = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={
        'multiple': True,
        'accept': '.txt',
    }))

    def clean(self):
        cleaned_data = super(UpdateSelectForm, self).clean()
        status = cleaned_data.get('status')
        optional_status = cleaned_data.get('optional_status')
        ids = cleaned_data.get('ids')
        if ids is not None:
            if re.findall(r'[.,:,-,,]', ids):
                self.add_error('ids', 'Allowed are only - or ;')

    def save(self, commit=True):
        m = super(UpdateSelectForm, self).save(commit=False)
        m.last_change = datetime.today()
        m.save()
        return m


class UpdateSelectFormWithoutBoxNumber(forms.ModelForm):
    class Meta:
        model = PriolisteAssignment
        fields = ['status', 'optional_status', 'staff', 'co_worker', 'ordering_number', 'box', 'customer', 'hardware',
                  'production_remark', 'remark', 'last_change', 'created_at', 'finished_until',
                  'prod_rec_one', 'prod_rec_two', 'prod_rec_three', 'prod_rec_four', 'prod_rec_five', ]
        labels = {
            'box': _('Kiste: '),
            'customer': _('Kunde: '),
            'hardware': _('Hardware: '),
            'created_at': _('Erstellt am: '),
            'status': _('Status: '),
            'optional_status': _('Status: '),
            'finished_until': _('Fertig bis: '),
            'staff': _('erstellt von Mitarbeiter: '),
            'time_in_weeks': _('Zeit in Wochen: '),
            'production_remark': 'Production remark - for production ONLY',
            'remark': 'Sales remark - for sales ONLY',
        }
        widgets = {
            'last_change': forms.TextInput(attrs={'readonly': 'readonly'}),
            'created_at': forms.TextInput(attrs={'readonly': 'readonly'}),
            'staff': forms.Select(choices=STAFFCHOICESONE),
            'co_worker': forms.Select(choices=STAFFCHOICESTWO),
        }

    def clean(self):
        cleaned_data = super(UpdateSelectFormWithoutBoxNumber, self).clean()
        status = cleaned_data.get('status')
        optional_status = cleaned_data.get('optional_status')
        created_at = cleaned_data.get('created_at')
        finished_until = cleaned_data.get('finished_until')
        assignment = PriolisteAssignment.objects.get(pk=self.instance.pk)
        # if status is None:
        #     if optional_status is None:
        #         self.add_error('status', 'Please select a status')
        #         self.add_error('optional_status', 'Or type in an optional_status')
        if assignment.time_in_weeks is not None:
            if update_time_in_weeks(created_at, finished_until) < assignment.time_in_weeks:
                self.add_error('finished_until', 'Date cannot be in the past, \nif it really should be contact the Produktion-Team')

    def save(self, commit=True):
        m = super(UpdateSelectFormWithoutBoxNumber, self).save(commit=False)
        m.last_change = datetime.today()
        m.time_in_weeks = update_time_in_weeks(m.created_at, m.finished_until)
        m.save()
        return m


class CheckProductionStatus(forms.ModelForm):
    class Meta:
        model = PriolisteAssignment
        fields = ['belt', 'batterie', 'elektronic']
        labels = {
            'belt': 'Gurt',
            'batterie': 'Batterie',
            'elektronic': 'Elektronik',
            'assembled': 'Zusammengebaut'
        }


class UpdateDoneForm(forms.ModelForm):
    class Meta:
        model = PriolisteAssignment
        fields = ['staff', 'status', 'remark', ]
        widgets = {
            'staff': forms.Select(choices=STAFFCHOICESONE),
        }


BATTERIECHOICES = (
    ('------', '------'),
)

TYPECHOICES = (
    ('Vertex Plus IR', 'Vertex Plus IR'),
    ('Vertex Plus GL', 'Vertex Plus GL'),
    ('Vertex Plus GSM', 'Vertex Plus GSM'),
    ('Vertex Lite IR', 'Vertex Lite IR'),
    ('Vertex Lite GL', 'Vertex Lite GL'),
    ('Vertex Plus UHF', 'Vertex Plus UHF'),
    ('Vertex Plus SOB', 'Vertex Plus SOB'),
    ('Vertex Lite SOB', 'Vertex Lite SOB'),
    ('Vertex Lite GSM', 'Vertex Lite GSM'),
    ('Survey IR', 'Survey IR'),
    ('Survey GL', 'Survey GL'),
    ('Survey GSM', 'Survey GSM'),
    ('Aufarbeitung', 'Aufarbeitung'),
    ('TT', 'TrapTransmitter'),
    #('TT', 'TT GS'),
    #('TT', 'TT IR'),
    ('MIT', 'MIT'),
    ('VIT', 'VIT'),
    ('RIT FIWI', 'RIT FIWI'),
    ('Fawn', 'Fawn'),
    ('Mini-Fawn GL', 'Mini-Fawn GL'),
    ('Tag', 'Tag'),
    ('ActLogger', 'ActLogger'),
    ('Elephanten', 'Elephanten'),
    ('Batterien', 'Batterien'),
    ('Dummy', 'Dummy'),
    ('Testen', 'Testen'),
)

ADDON = (
    ('', ''),
    ('Kamera', 'Camera'),
    ('FIWI Repeater', 'FIWI Repeater'),
    ('Dosimeter', 'Dosimeter'),
)


class BatterieSearchForm(forms.Form):
    batterie_type = forms.ChoiceField(choices=BATTERIECHOICES + TYPECHOICES + ADDON[1:], label='Hardware', required=False)


class Search_Everything(forms.Form):
    to_search = forms.CharField(label='Search', required=False)


class HardwareCreateForm(forms.Form):
    number = forms.IntegerField(label='Quantity', required=False)
    type = forms.ChoiceField(choices=TYPECHOICES, label='Hardware Type', required=False)
    batterie = forms.CharField(label='Batterie', required=False)
    addon = forms.ChoiceField(choices=ADDON, label='Batterie AddOn', required=False, initial='')
    droppOff = forms.BooleanField(required=False, initial=False, label='Drop Off')
    externDropOff = forms.BooleanField(required=False, initial=False, label='External Drop Off')
    prodRecOne = forms.FileField(required=False, allow_empty_file=True)
    
    def clean(self):
        cleaned_data = super(HardwareCreateForm, self).clean()


class BaseLinkFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        for form in self.forms:
            if form.cleaned_data:
                number = form.cleaned_data['number']
                type = form.cleaned_data['type']
                number = form.cleaned_data['batterie']
                type = form.cleaned_data['droppOff']
                type = form.cleaned_data['prodRecOne']

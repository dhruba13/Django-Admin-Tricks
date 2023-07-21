from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ProductAdminForm(forms.ModelForm):
    last_state = forms.CharField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(self.instance, 'pk', None):
            self.initial['last_state'] = getattr(self.instance, 'state', None)

    def clean_last_state(self):
        if self.cleaned_data['last_state'] != str(self.initial['last_state']):
            self.add_error(None, ValidationError(_('Somebody change this object already')))

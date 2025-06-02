from django import forms
from .models import Mitgliedsantrag
import re
from stdnum import iban as stdnum_iban
from stdnum import bic as stdnum_bic


class MitgliedsantragForm(forms.ModelForm):
    class Meta:
        model = Mitgliedsantrag
        exclude = ["pdf_datei", "erstellt_am", "unterschrift"]

    
    def clean_iban(self):
        iban = self.cleaned_data.get('iban').replace(" ", "").upper()
        if not stdnum_iban.is_valid(iban):
            raise forms.ValidationError("Bitte eine gültige IBAN angeben.")
        return iban

    def clean_bic(self):
        bic = self.cleaned_data.get('bic').replace(" ", "").upper()
        if not stdnum_bic.is_valid(bic):
            raise forms.ValidationError("Bitte eine gültige BIC angeben (8 oder 11 Zeichen).")
        return bic
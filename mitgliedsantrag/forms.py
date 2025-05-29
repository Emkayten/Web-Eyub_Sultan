from django import forms
from .models import Mitgliedsantrag

class MitgliedsantragForm(forms.ModelForm):
    class Meta:
        model = Mitgliedsantrag
        exclude = ["pdf_datei", "erstellt_am", "unterschrift"]

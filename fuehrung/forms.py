from django import forms
from .models import Moscheefuehrung

class MoscheefuehrungForm(forms.ModelForm):
    class Meta:
        model = Moscheefuehrung
        fields = [
            'einrichtung',
            'ansprechperson',
            'email',
            'telefon',
            'teilnehmerzahl',
            'wunschtermin',
            'uhrzeit',
            'nachricht',
        ]
        widgets = {
            'wunschtermin': forms.DateInput(attrs={'type': 'date'}),
            'uhrzeit': forms.TimeInput(attrs={'type': 'time'}),
            'nachricht': forms.Textarea(attrs={'rows': 4}),
            'telefon': forms.TextInput(attrs={'placeholder': 'z. B. +49 123 4567890'}),
        }

        

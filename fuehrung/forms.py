from django import forms
from .models import Moscheefuehrung
from django.utils import timezone
from datetime import time

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
            'wunschtermin': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': timezone.localdate().strftime('%Y-%m-%d'),  # Datumsauswahl erst ab heute
                }
            ),
            'uhrzeit': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'step': 900  # 900 Sekunden = 15 Minuten
                }
            ),
            'nachricht': forms.Textarea(attrs={'rows': 4}),
            'telefon': forms.TextInput(attrs={'placeholder': 'z. B. +49 123 4567890'}),
        }

    def clean_wunschtermin(self):
        datum = self.cleaned_data.get('wunschtermin')
        if datum and datum < timezone.localdate():
            raise forms.ValidationError("Der Wunschtermin muss in der Zukunft liegen.")
        return datum

    def clean_uhrzeit(self):
        uhrzeit = self.cleaned_data.get('uhrzeit')
        if uhrzeit:
            # Uhrzeit nur zwischen 9:00 und 20:00 Uhr
            if not (time(9, 0) <= uhrzeit <= time(20, 0)):
                raise forms.ValidationError("Die Uhrzeit muss zwischen 9:00 und 20:00 Uhr liegen.")
            # Minuten müssen 00, 15, 30 oder 45 sein
            if uhrzeit.minute not in (0, 15, 30, 45):
                raise forms.ValidationError("Die Minuten müssen 00, 15, 30 oder 45 sein.")
        return uhrzeit

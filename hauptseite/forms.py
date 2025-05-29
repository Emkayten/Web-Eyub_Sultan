from django import forms
from .models import KontaktNachricht

class KontaktForm(forms.ModelForm):
    class Meta:
        model = KontaktNachricht
        fields = ['name', 'email', 'nachricht']
        widgets = {
            'nachricht': forms.Textarea(attrs={'rows': 5}),
        }

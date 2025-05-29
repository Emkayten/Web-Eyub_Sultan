from django.shortcuts import render
from .models import VorstandMitglied

def vorstand_view(request):
    gruppen = {
        'leiter': VorstandMitglied.objects.filter(rolle='leiter'),
        'verwaltung': VorstandMitglied.objects.filter(rolle='verwaltung'),
        'vorstand': VorstandMitglied.objects.filter(rolle='vorstand'),
    }
    return render(request, 'gemeinde/vorstand.html', {'gruppen': gruppen})

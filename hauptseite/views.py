from django.shortcuts import render, redirect, get_object_or_404
from .models import Neuigkeit
from django.http import JsonResponse
from .forms import KontaktForm
from django.contrib import messages

def startseite(request):
    neuigkeiten = Neuigkeit.objects.all().order_by('-erstellt_am')[:5]
    return render(request, 'hauptseite/startseite.html', {'neuigkeiten': neuigkeiten})

def neuigkeit_hinzufuegen(request):
    if request.method == 'POST':
        titel = request.POST.get('titel')
        inhalt = request.POST.get('inhalt')
        bild = request.FILES.get('bild')  # Bild kann optional sein
        
        neuigkeit = Neuigkeit(titel=titel, inhalt=inhalt)
        if bild:
            neuigkeit.bild = bild
        neuigkeit.save()
        
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def neuigkeit_detail(request, pk):
    neuigkeit = get_object_or_404(Neuigkeit, pk=pk)
    return render(request, 'hauptseite/neuigkeit_detail.html', {'neuigkeit': neuigkeit})


def kontakt_view(request):
    if request.method == 'POST':
        form = KontaktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kontakt_danke')
    else:
        form = KontaktForm()
    return render(request, 'hauptseite/kontakt.html', {'form': form})

def kontakt_danke(request):
    return render(request, 'hauptseite/kontakt_danke.html')

def impressum(request):
    return render(request, 'hauptseite/impressum.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Neuigkeit
from django.http import JsonResponse
from .forms import KontaktForm
from django.contrib import messages
from django.utils import timezone
from kalender.models import Event
from datetime import timedelta

def startseite(request):
    # Neuigkeiten laden
    neuigkeiten = Neuigkeit.objects.all().order_by('-erstellt_am')[:5]

    # Kalender-Logik
    heute = timezone.localdate()
    start_param = request.GET.get('start')

    if start_param:
        try:
            wochenstart = timezone.datetime.strptime(start_param, "%Y-%m-%d").date()
        except ValueError:
            wochenstart = heute - timedelta(days=heute.weekday())
    else:
        wochenstart = heute - timedelta(days=heute.weekday())

    wochenende = wochenstart + timedelta(days=6)
    events = Event.objects.filter(date__range=[wochenstart, wochenende]).order_by('date', 'start_time')
    wochentage = [wochenstart + timedelta(days=i) for i in range(7)]
    prev_week = wochenstart - timedelta(days=7)
    next_week = wochenstart + timedelta(days=7)

    context = {
        "neuigkeiten": neuigkeiten,
        "wochenstart": wochenstart,
        "wochenende": wochenende,
        "wochentage": wochentage,
        "events": events,
        "prev_week": prev_week,
        "next_week": next_week,
    }

    # Wichtig: richtiger Template-Pfad!
    return render(request, "hauptseite/startseite.html", context)

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

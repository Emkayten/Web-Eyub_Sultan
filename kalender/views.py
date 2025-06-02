from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Event
from datetime import timedelta, datetime
import logging
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)  # Logging initialisieren

def wochenansicht(request):
    start_param = request.GET.get('start')
    logger.info(f"Empfangener start_param: {start_param}")

    if start_param:
        try:
            # Versuche das Datum zu parsen
            wochenstart = datetime.strptime(start_param, "%Y-%m-%d").date()
            logger.info(f"Parsed wochenstart: {wochenstart}")
        except ValueError:
            # Fallback: heutige Woche
            logger.warning("Ungültiges Datumsformat! Fallback auf aktuelle Woche.")
            heute = timezone.localdate()
            wochenstart = heute - timedelta(days=heute.weekday())
    else:
        # Kein Parameter übergeben: Standard = aktuelle Woche
        heute = timezone.localdate()
        wochenstart = heute - timedelta(days=heute.weekday())
        logger.info(f"Standard wochenstart: {wochenstart}")

    wochenende = wochenstart + timedelta(days=6)

    # Events laden
    events = Event.objects.filter(date__range=[wochenstart, wochenende]).order_by('date', 'start_time')

    # 7 Tage der Woche generieren
    wochentage = [wochenstart + timedelta(days=i) for i in range(7)]

    # Vorherige & nächste Woche
    prev_week = wochenstart - timedelta(days=7)
    next_week = wochenstart + timedelta(days=7)

    context = {
        "events": events,
        "wochenstart": wochenstart,
        "wochenende": wochenende,
        "wochentage": wochentage,
        "prev_week": prev_week,
        "next_week": next_week,
    }
    return render(request, "kalender/wochenansicht.html", context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.models import UserProfile, Role
from django.contrib.auth.models import User
from django.contrib import messages
from downloads.models import Download
from hauptseite.models import Neuigkeit, KontaktNachricht
from fuehrung.models import Moscheefuehrung
from mitgliedsantrag.models import Mitgliedsantrag
from gemeinde.models import VorstandMitglied
from kalender.models import Event
from django.utils import timezone
from datetime import timedelta

@login_required
def admin_dashboard(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')  # oder eigene „Kein Zugriff“-Seite

    return render(request, 'adminpanel/adminpanel_base.html')




@login_required
def benutzerverwaltung(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    profiles = UserProfile.objects.select_related('user').prefetch_related('roles').all()
    roles = Role.objects.all()

    if request.method == 'POST':
        for profile in profiles:
            rollen_ids = request.POST.getlist(f'roles_{profile.id}')
            profile.roles.set(rollen_ids)  # Rollen updaten!
        return redirect('admin_benutzerverwaltung')  # Nach dem Speichern zurück

    return render(request, 'adminpanel/benutzerverwaltung.html', {
        'profiles': profiles,
        'roles': roles,
    })

from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def benutzer_hinzufuegen(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwörter stimmen nicht überein!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Benutzername bereits vergeben!")
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Benutzer erfolgreich erstellt!")
    
    return redirect('admin_benutzerverwaltung')

@login_required
def downloads_verwaltung(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    if request.method == 'POST':
        # Neuer Download
        beschreibung = request.POST.get('beschreibung')
        pdf = request.FILES.get('pdf')
        if beschreibung and pdf:
            Download.objects.create(beschreibung=beschreibung, pdf=pdf)
            messages.success(request, "Download erfolgreich hinzugefügt!")
            return redirect('admin_downloads')

        # Löschen eines bestehenden Eintrags
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                download = Download.objects.get(id=delete_id)
                download.delete()
                messages.success(request, "Download gelöscht!")
            except Download.DoesNotExist:
                messages.error(request, "Download nicht gefunden.")
            return redirect('admin_downloads')

    downloads = Download.objects.all()
    return render(request, 'adminpanel/downloads.html', {
        'downloads': downloads
    })

@login_required
def neuigkeiten_verwaltung(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    if request.method == 'POST':
        # Neuen Eintrag erstellen
        if 'titel' in request.POST:
            titel = request.POST.get('titel')
            inhalt = request.POST.get('inhalt')
            bild = request.FILES.get('bild')
            neuigkeit = Neuigkeit(titel=titel, inhalt=inhalt)
            if bild:
                neuigkeit.bild = bild
            neuigkeit.save()
            messages.success(request, "Neuigkeit erfolgreich hinzugefügt!")
            return redirect('admin_neuigkeiten')

        # Löschen eines Eintrags
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                neuigkeit = Neuigkeit.objects.get(id=delete_id)
                neuigkeit.delete()
                messages.success(request, "Neuigkeit gelöscht!")
            except Neuigkeit.DoesNotExist:
                messages.error(request, "Neuigkeit nicht gefunden.")
            return redirect('admin_neuigkeiten')

    neuigkeiten = Neuigkeit.objects.all().order_by('-erstellt_am')
    return render(request, 'adminpanel/neuigkeiten.html', {
        'neuigkeiten': neuigkeiten
    })

@login_required
def kontakt_verwaltung(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    # Bearbeitungsstatus ändern
    if request.method == 'POST':
        mark_id = request.POST.get('mark_id')
        if mark_id:
            try:
                nachricht = KontaktNachricht.objects.get(id=mark_id)
                nachricht.bearbeitet = not nachricht.bearbeitet  # Status toggeln
                nachricht.save()
                messages.success(request, "Bearbeitungsstatus geändert!")
            except KontaktNachricht.DoesNotExist:
                messages.error(request, "Nachricht nicht gefunden.")
            return redirect('admin_kontakt')

    nachrichten = KontaktNachricht.objects.all().order_by('-erstellt_am')
    return render(request, 'adminpanel/kontakt.html', {
        'nachrichten': nachrichten
    })

@login_required
def fuehrung_verwaltung(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    if request.method == 'POST':
        mark_id = request.POST.get('mark_id')
        if mark_id:
            try:
                fuehrung = Moscheefuehrung.objects.get(id=mark_id)
                fuehrung.bearbeitet = not fuehrung.bearbeitet
                fuehrung.save()
                messages.success(request, "Bearbeitungsstatus geändert!")
            except Moscheefuehrung.DoesNotExist:
                messages.error(request, "Eintrag nicht gefunden.")
            return redirect('admin_fuehrung')

    fuehrungen = Moscheefuehrung.objects.all().order_by('-erstellt_am')
    return render(request, 'adminpanel/fuehrung.html', {
        'fuehrungen': fuehrungen
    })

@login_required
def mitgliedsantrag_verwaltung(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    if request.method == 'POST':
        mark_id = request.POST.get('mark_id')
        if mark_id:
            try:
                antrag = Mitgliedsantrag.objects.get(id=mark_id)
                antrag.bearbeitet = not antrag.bearbeitet
                antrag.save()
                messages.success(request, "Bearbeitungsstatus geändert!")
            except Mitgliedsantrag.DoesNotExist:
                messages.error(request, "Antrag nicht gefunden.")
            return redirect('admin_mitgliedsantrag')

    antraege = Mitgliedsantrag.objects.all().order_by('-erstellt_am')
    return render(request, 'adminpanel/mitgliedsantrag.html', {
        'antraege': antraege
    })

@login_required
def vorstand_verwaltung(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    mitglieder = VorstandMitglied.objects.all()

    if request.method == 'POST':
        # Neuen Eintrag anlegen
        if 'name' in request.POST:
            name = request.POST.get('name')
            aufgabe = request.POST.get('aufgabe')
            rolle = request.POST.get('rolle')
            geschlecht = request.POST.get('geschlecht')
            bild = request.FILES.get('bild')
            mitglied = VorstandMitglied(name=name, aufgabe=aufgabe, rolle=rolle, geschlecht=geschlecht)
            if bild:
                mitglied.bild = bild
            mitglied.save()
            messages.success(request, "Neues Mitglied angelegt!")
            return redirect('admin_vorstand')

        # Löschen
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                Mitglied = VorstandMitglied.objects.get(id=delete_id)
                Mitglied.delete()
                messages.success(request, "Mitglied gelöscht!")
            except VorstandMitglied.DoesNotExist:
                messages.error(request, "Mitglied nicht gefunden!")
            return redirect('admin_vorstand')

    return render(request, 'adminpanel/vorstand.html', {
        'mitglieder': mitglieder
    })

@login_required
def kalender_adminpanel(request):
    if not request.user.userprofile.roles.filter(name='admin').exists():
        return render(request, '403.html')

    events = Event.objects.all().order_by('-date', 'start_time')

    if request.method == 'POST':
        if 'title' in request.POST:
            title = request.POST.get('title')
            date = request.POST.get('date')
            start_time = request.POST.get('start_time') or None
            end_time = request.POST.get('end_time') or None
            description = request.POST.get('description')

            Event.objects.create(
                title=title,
                date=date,
                start_time=start_time,
                end_time=end_time,
                description=description
            )
            messages.success(request, "Neuer Kalendereintrag hinzugefügt!")
            return redirect('admin_kalender')

        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                event = Event.objects.get(id=delete_id)
                event.delete()
                messages.success(request, "Kalendereintrag gelöscht!")
            except Event.DoesNotExist:
                messages.error(request, "Kalendereintrag nicht gefunden!")
            return redirect('admin_kalender')

    return render(request, 'adminpanel/kalender.html', {
        'events': events
    })
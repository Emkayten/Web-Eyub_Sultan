from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import LoginForm
from .models import UserProfile
from django.contrib.auth.models import User

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                profile, _ = UserProfile.objects.get_or_create(user=user)
            except User.DoesNotExist:
                messages.error(request, "Ungültige Zugangsdaten!")
                return render(request, 'accounts/login.html', {'form': form})
            
            if profile.is_locked_out():
                messages.error(request, "Konto vorübergehend gesperrt. Bitte warte 10 Minuten.")
                return render(request, 'accounts/login.html', {'form': form})
            
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    messages.error(request, "Konto deaktiviert!")
                else:
                    profile.reset_attempts()
                    login(request, user)
                    messages.success(request, f"Willkommen, {username}!")
                    return redirect('startseite')
            else:
                profile.failed_attempts += 1
                if profile.failed_attempts >= 5:
                    if profile.sperre_count == 0:
                        profile.lockout_until = timezone.now() + timezone.timedelta(minutes=10)
                        profile.failed_attempts = 0  # Reset nach Sperre
                        profile.sperre_count = 1
                        messages.error(request, "5 Fehlversuche: Konto für 10 Minuten gesperrt.")
                    else:
                        user.is_active = False
                        user.save()
                        messages.error(request, "Zweiter Block: Konto deaktiviert!")
                profile.save()
    return render(request, 'accounts/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('startseite')  # oder deine Hauptseite

def startseite(request):
    is_admin = False
    is_verwaltung = False
    is_media = False
    is_hoca = False

    if request.user.is_authenticated:
        user_roles = request.user.userprofile.roles.values_list('name', flat=True)
        is_admin = 'admin' in user_roles
        is_verwaltung = 'verwaltung' in user_roles
        is_media = 'media' in user_roles
        is_hoca = 'hoca' in user_roles

    return render(request, 'dein_template.html', {
        'is_admin': is_admin,
        'is_verwaltung': is_verwaltung,
        'is_media': is_media,
        'is_hoca': is_hoca,
    })

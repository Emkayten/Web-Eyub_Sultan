from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MoscheefuehrungForm

def fuehrung_anfrage(request):
    if request.method == 'POST':
        form = MoscheefuehrungForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vielen Dank für Ihre Anmeldung!")
            return redirect('anfrage_danke')
    else:
        form = MoscheefuehrungForm()

    return render(request, 'fuehrung/anfrage.html', {'form': form})

def anfrage_danke(request):
    return render(request, 'fuehrung/anfrage_danke.html')

from django.shortcuts import render
from .models import Download

def downloads_view(request):
    downloads = Download.objects.all()
    fest_elemente = [
        {"titel": "Festes PDF 1", "link": "/static/pdf/festes1.pdf"},
        {"titel": "Festes PDF 2", "link": "/static/pdf/festes2.pdf"},
    ]
    return render(request, 'downloads/downloads.html', {
        'downloads': downloads,
        'fest_elemente': fest_elemente,
    })

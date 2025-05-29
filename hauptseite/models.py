from django.db import models
from django.utils import timezone

class Neuigkeit(models.Model):
    titel = models.CharField(max_length=200)
    inhalt = models.TextField()
    bild = models.ImageField(upload_to='neuigkeiten_bilder/', blank=True, null=True)
    erstellt_am = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titel

class KontaktNachricht(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    nachricht = models.TextField()
    erstellt_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.erstellt_am.strftime('%Y-%m-%d %H:%M')}"
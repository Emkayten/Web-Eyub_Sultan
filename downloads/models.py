from django.db import models

class Download(models.Model):
    beschreibung = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='downloads/')

    def __str__(self):
        return self.beschreibung

from django.db import models
from django.core.validators import RegexValidator


class Moscheefuehrung(models.Model):
    einrichtung = models.CharField("Name der Einrichtung / Schule", max_length=200)
    ansprechperson = models.CharField("Ansprechperson", max_length=100)
    email = models.EmailField("E-Mail-Adresse")
    telefon = models.CharField(
    "Telefonnummer",
    max_length=50,
    blank=True,
    validators=[
        RegexValidator(
            regex=r'^[0-9+() -]+$',
            message="Bitte eine gültige Telefonnummer eingeben (nur Ziffern, +, (), - und Leerzeichen erlaubt)."
        )
    ]
)

    teilnehmerzahl = models.PositiveIntegerField("Anzahl der Teilnehmer")
    wunschtermin = models.DateField("Wunschtermin")
    uhrzeit = models.TimeField("Uhrzeit", blank=True, null=True)
    nachricht = models.TextField("Nachricht / Anliegen", blank=True)
    erstellt_am = models.DateTimeField(auto_now_add=True)
    bearbeitet = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.einrichtung} – {self.wunschtermin}"
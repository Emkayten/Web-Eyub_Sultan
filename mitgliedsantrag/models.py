from django.db import models

class Mitgliedsantrag(models.Model):
    name = models.CharField("Name und Vorname", max_length=255)
    adresse = models.CharField("Adresse", max_length=255)
    mobilnummer = models.CharField("Mobilnummer", max_length=20)
    kontoinhaber = models.CharField("Kontoinhaber", max_length=255)
    iban = models.CharField("IBAN", max_length=34)
    bic = models.CharField("BIC", max_length=11)
    beitrag = models.DecimalField("Monatlicher Beitrag", max_digits=5, decimal_places=2)
    zahlungstermin = models.CharField(
        "Zahlungstermin",
        max_length=10,
        choices=[("1.", "1. des Monats"), ("15.", "15. des Monats")],
        default="1."
    )
    unterschrift = models.ImageField("Unterschrift", upload_to='mitgliedsantrag/signaturen/', blank=True, null=True)
    unterschrift2 = models.ImageField("2. Unterschrift", upload_to='mitgliedsantrag/signaturen/', blank=True, null=True)

    pdf_datei = models.FileField("PDF-Datei", upload_to='mitgliedsantrag/pdfs/')
    erstellt_am = models.DateTimeField("Erstellt am", auto_now_add=True)
    bearbeitet = models.BooleanField(default=False)


    def __str__(self):
        return f"Mitgliedsantrag von {self.name} am {self.erstellt_am.date()}"
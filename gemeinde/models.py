from django.db import models

class VorstandMitglied(models.Model):
    ROLLEN = [
        ('leiter', 'Leiter'),
        ('verwaltung', 'Verwaltung'),
        ('vorstand', 'Vorstand'),
    ]

    GESCHLECHTER = [
        ('maennlich', 'Männlich'),
        ('weiblich', 'Weiblich'),
    ]

    name = models.CharField(max_length=100)
    aufgabe = models.TextField()
    rolle = models.CharField(max_length=20, choices=ROLLEN)
    geschlecht = models.CharField(max_length=10, choices=GESCHLECHTER)
    bild = models.ImageField(upload_to='vorstandsbilder/', blank=True, null=True)

    class Meta:
        verbose_name = "Vorstandsmitglied"
        verbose_name_plural = "Vorstandsmitglieder"
        ordering = ['rolle', 'name']

    def __str__(self):
        return self.name

    def bild_url(self):
        if self.bild:
            return self.bild.url
        elif self.geschlecht == 'weiblich':
            return '/static/images/female.png'
        else:
            return '/static/images/male.png'
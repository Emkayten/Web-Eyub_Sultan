from django.contrib import admin
from .models import Mitgliedsantrag

@admin.register(Mitgliedsantrag)
class MitgliedsantragAdmin(admin.ModelAdmin):
    list_display = ("name", "adresse", "mobilnummer", "erstellt_am")
    readonly_fields = ("unterschrift", "unterschrift2", "pdf_datei")

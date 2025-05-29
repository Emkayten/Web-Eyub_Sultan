from django.contrib import admin
from .models import Moscheefuehrung

@admin.register(Moscheefuehrung)
class MoscheefuehrungAdmin(admin.ModelAdmin):
    list_display = ('einrichtung', 'ansprechperson', 'email', 'wunschtermin', 'teilnehmerzahl', 'erstellt_am')
    list_filter = ('wunschtermin', 'erstellt_am')
    search_fields = ('einrichtung', 'ansprechperson', 'email')

from django.contrib import admin
from .models import Neuigkeit, KontaktNachricht

@admin.register(Neuigkeit)
class NeuigkeitAdmin(admin.ModelAdmin):
    list_display = ('titel', 'erstellt_am')
    search_fields = ('titel', 'inhalt')
    list_filter = ('erstellt_am',)

@admin.register(KontaktNachricht)
class KontaktNachrichtAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'nachricht', 'erstellt_am')
    search_fields = ('name', 'email', 'nachricht')
    list_filter = ('erstellt_am',)
    readonly_fields = ('name', 'email', 'nachricht', 'erstellt_am')
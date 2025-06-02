from django.urls import path
from .views import admin_dashboard
from .views import admin_dashboard, benutzerverwaltung, benutzer_hinzufuegen, downloads_verwaltung, neuigkeiten_verwaltung,kontakt_verwaltung, fuehrung_verwaltung, mitgliedsantrag_verwaltung, vorstand_verwaltung, kalender_adminpanel


urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('benutzerverwaltung/', benutzerverwaltung, name='admin_benutzerverwaltung'),
    path('benutzer/hinzufuegen/', benutzer_hinzufuegen, name='admin_benutzer_hinzufuegen'),
     path('downloads/', downloads_verwaltung, name='admin_downloads'),
     path('neuigkeiten/', neuigkeiten_verwaltung, name='admin_neuigkeiten'),
     path('kontakt/', kontakt_verwaltung, name='admin_kontakt'),
    path('fuehrung/', fuehrung_verwaltung, name='admin_fuehrung'),
    path('mitgliedsantrag/', mitgliedsantrag_verwaltung, name='admin_mitgliedsantrag'),
    path('vorstand/', vorstand_verwaltung, name='admin_vorstand'),
    path('kalender/', kalender_adminpanel, name='admin_kalender'),
]


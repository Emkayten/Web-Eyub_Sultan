from django.urls import path
from . import views

urlpatterns = [
    path('', views.startseite, name='startseite'),
    path('neuigkeit-hinzufuegen/', views.neuigkeit_hinzufuegen, name='neuigkeit_hinzufuegen'),
    path('kontakt/', views.kontakt_view, name='kontakt'),
    path('kontakt/danke/', views.kontakt_danke, name='kontakt_danke'),
     path('neuigkeit/<int:pk>/', views.neuigkeit_detail, name='neuigkeit_detail'),
     path('impressum/', views.impressum, name='impressum'),
]

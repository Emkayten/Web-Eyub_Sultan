from django.urls import path
from . import views

urlpatterns = [
    path('anmeldung/', views.fuehrung_anfrage, name='fuehrung_anfrage'),
    path('danke/', views.anfrage_danke, name='anfrage_danke'),

]

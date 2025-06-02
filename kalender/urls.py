from django.urls import path
from . import views

urlpatterns = [
    path("", views.wochenansicht, name="wochenansicht"),
]

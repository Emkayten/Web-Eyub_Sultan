from django.urls import path
from . import views

urlpatterns = [
    path("", views.mitgliedsantrag_view, name="mitgliedsantrag"),
    path("erfolg/", views.mitgliedsantrag_success, name="mitgliedsantrag_success"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('vorstand/', views.vorstand_view, name='vorstand'),
]

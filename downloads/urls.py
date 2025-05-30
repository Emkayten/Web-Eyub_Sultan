from django.urls import path
from .views import downloads_view

urlpatterns = [
    path('', downloads_view, name='downloads'),
]

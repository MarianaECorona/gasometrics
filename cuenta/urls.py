from .views import register
from django.urls import path, include

urlpatterns = [
    path('registro', register, name='register'),  # Registrar usuario
]

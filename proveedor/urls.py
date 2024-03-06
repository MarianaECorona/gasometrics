from django.urls import path, re_path
from .views import index, view_dashboard

urlpatterns = [
    path('', index),
    path('dashboard', view_dashboard, name= 'dashboard'),
]

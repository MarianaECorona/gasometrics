from django.urls import path, re_path
from .views import index, home

urlpatterns = [
    path('', index),
    path('home', home),
]

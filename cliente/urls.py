from django.urls import path, re_path
from .views import index, home, medicion

urlpatterns = [
    path('', index),
    path('home', home, name='main'),
    path('medicion', medicion, name='medicion')
]

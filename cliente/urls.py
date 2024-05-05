from django.urls import path, re_path
from .views import index, home, medicion, test

urlpatterns = [
    path('', index),
    path('home', home, name='main'),
    path('medicion', medicion, name='medicion'),
    path('test', test, name='test'),
]

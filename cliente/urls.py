from django.urls import path, re_path
from .views import index, home, pedido

urlpatterns = [
    path('', index),
    path('home', home, name='main'),
    path('pedido', pedido),
]

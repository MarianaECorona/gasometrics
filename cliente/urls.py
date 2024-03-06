from django.urls import path, re_path
from .views import index, home, solicitud_pedido, medicion

urlpatterns = [
    path('', index),
    path('home', home, name='main'),
    path('solicitud_pedido', solicitud_pedido, name='pedido_form'),
    path('medicion', medicion, name='medicion')
]

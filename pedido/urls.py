from django.urls import path
from .views import sumary

urlpatterns = [
    path('resumen_pedido', sumary, name='resumen_pedido')

]

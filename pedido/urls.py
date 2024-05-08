from django.urls import path
from . import views

urlpatterns = [
    path('resumen_pedido/<int:id_post>', views.sumary, name='resumen_pedido'),
    path('proceso_pago/<int:pedido_id>/', views.payment_process, name='pago'),
    path('pago_exitoso/', views.pago_exitoso, name='pago_exitoso'),
]

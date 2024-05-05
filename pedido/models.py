from django.db import models
from cuenta.models import Cuenta

class Pedido(models.Model):
    # Id
    id_pedido = models.BigAutoField(primary_key=True),
    # id cliente
    id_cliente = models.ForeignKey(Cuenta, on_delete=models.CASCADE, default=None)
    # id proveedor
    id_proveedor = models.ForeignKey(Cuenta, on_delete=models.CASCADE, default=None)
    # cantidad_litros
    cantidad_litros = models.IntegerField()
    # total
    total = models.FloatField(default=0.0)
    # fecha
    fecha = models.DateTimeField(auto_now_add=True)

# Create your models here.

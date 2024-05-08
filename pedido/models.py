from django.db import models
from django.conf import settings
from proveedor.models import Post

class Pedido(models.Model):
    class Meta:
        db_table = 'pedido'
    id_pedido = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    litros = models.PositiveSmallIntegerField()
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    post_ref = models.ForeignKey(Post, on_delete=models.CASCADE)

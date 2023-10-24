from django.db import models

class Fotos(models.Model):
    class Meta:
        db_table='Fotos'
    id_fotos = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ruta = models.CharField(max_length=254)

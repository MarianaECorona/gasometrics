from django.db import models

class Administrador(models.Model):
    class Meta:
        db_table='Administrador'
    id_administrador = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=254)
    correo = models.EmailField(max_length=254)
from django.db import models

class Proveedor(models.Model):
    class Meta:
        db_table='Proveedor'
    id_proveedor = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    contrasenia = models.CharField(max_length=254)
    precio_litro = models.CharField(max_length=5)
    correo = models.EmailField(max_length=254)
    rfc = models.CharField(max_length=13)
    calle = models.CharField(max_length=254)
    numero_interior = models.CharField(max_length=10)
    numero_exterior = models.CharField(max_length=10)
    codigo_postal = models.CharField(max_length=6)
    ciudad = models.CharField(max_length=15)
    colonia = models.CharField(max_length=254)

    def domicilio(self):
        return f'{self.calle} {self.numero_interior}{self.numero_exterior}, {self.colonia}, {self.codigo_postal}, {self.ciudad}'

    def __str__(self):
        return self.domicilio()
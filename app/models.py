from django.db import models

# Create your models here.
#cada clase en models.py se convierte en una table en la base de datos, esta se llamara automaticamente nombreapp_nombreclase

class Empleado(models.Model):
    nombre= models.CharField(max_length=100)
    edad= models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    

    def __str__(self):
        return f"{self.nombre} - {self.email}"


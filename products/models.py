from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=100, 
        verbose_name='Producto'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    image = models.ImageField(
        verbose_name='Imagen', 
        upload_to="products"
    )
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de Creación'
    )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de Modificación'
    )
       
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ["-created"]
         
    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Product(models.Model):
    # id se coloca automaticamente
    title      = models.CharField(max_length=120)
    descripcion= models.TextField(blank=True,null=True)
    price      = models.DecimalField(decimal_places=2,max_digits=64)
    sumary     = models.TextField(blank=True,null=True)
    featured   = models.BooleanField(default=False)
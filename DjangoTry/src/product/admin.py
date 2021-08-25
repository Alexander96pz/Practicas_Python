from django.contrib import admin
from .models import Product
# Register your models here.
# UI del admin util para gestionar datos en la BD
admin.site.register(Product)

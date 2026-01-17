from django.contrib import admin
from .models import Categoria, Marca 

admin.site.register(Categoria)
admin.site.register(Marca)
# Eliminamos las líneas de Empleado, Producto y Pedido porque se manejan por PyMongo, no por el Admin
from django.contrib import admin
from .models import Vendedores, Productos, Clientes
# Register your models here.

admin.site.register(Vendedores)
admin.site.register(Productos)
admin.site.register(Clientes)
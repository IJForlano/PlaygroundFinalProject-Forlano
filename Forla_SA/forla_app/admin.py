from django.contrib import admin
from .models import Producto, Avatar


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio")
    list_filter = ("nombre", "precio")
    search_fields = ("nombre", "precio")


@admin.register(Avatar)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("user", "imagen")
    list_filter = ("user", "imagen")
    search_fields = ("user", "imagen")

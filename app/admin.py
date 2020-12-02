from django.contrib import admin
from .models import Productos,carruselImagene,Galeria,MisionyVision
# Register your models here.

class AdministradorProducto( admin.ModelAdmin ):
    list_display = ["nombre","precio","stock","imagen","Descripción"]
    search_fields = ["nombre","precio","stock","imagen","Descripción"]
    list_filter = ["nombre","precio","stock"]
    list_per_page = 10
    list_editable = ["precio","stock"]

class AdministradorcarruselImagene( admin.ModelAdmin ):
    list_display = ["nombre","imagen"]
    search_fields = ["nombre","imagen"]
    list_per_page = 10

class AdministradorGaleria( admin.ModelAdmin ):
    list_display = ["nombre","imagen"]
    search_fields = ["nombre","imagen"]
    list_per_page = 10

class AdinistradorMisionVision( admin.ModelAdmin ):
    list_display  = ["titulo","Descripcion"]
    search_fields = ["Titulo","Descripcion"]
    list_per_page = 10
    list_editable = ["Descripcion"]

admin.site.register(Productos, AdministradorProducto)
admin.site.register(carruselImagene,AdministradorcarruselImagene)
admin.site.register(Galeria, AdministradorGaleria)
admin.site.register(MisionyVision,AdinistradorMisionVision)

admin.site.site_header = "Auto Lavado Administración"
admin.site.site_title  = "AutoLavado"
admin.site.index_title = "Administracion del Sitio"
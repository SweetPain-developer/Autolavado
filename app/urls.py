from django.urls import path
from .views import home,misionVision,ubicacion,galeria,ingresarinsumos,registro,listar_Insumos,modificar_Insumos,eliminar_Insumos


urlpatterns = [
    path('', home, name="home"),
    path('misionVision/', misionVision, name="misionVision"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('galeria/', galeria, name="galeria"),
    path('insumos/', ingresarinsumos, name="insumos"),
    path('listar-insumos/', listar_Insumos, name="listar-insumos"),
    path('modificar-insumos/<id>/', modificar_Insumos, name="modificar-insumos"),
    path('eliminar-insumos/<id>/', eliminar_Insumos, name="eliminar-insumos"),
    path('registro/', registro, name="registro"),
    
]


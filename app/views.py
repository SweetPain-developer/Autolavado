from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import carruselImagene, Galeria, MisionyVision, Productos
from .forms import CustomUserCreationForm, ProductosFrom
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

def home(request):
    
    objeto = carruselImagene.objects.all()
    
    data = {
        "carrucel": objeto
    }

    return render(request, 'app/home.html', data)

def misionVision(request):

    objeto = MisionyVision.objects.all()
    
    data = {
        "mision": objeto
    }

    return render(request, 'app/misionVision.html', data)

def ubicacion(request):
    return render(request, 'app/ubicacion.html')

def galeria(request):

    objeto = Galeria.objects.all()

    data = {
        "galeria": objeto
    }

    return render(request, 'app/galeria.html', data)

@permission_required('app.add_productos')
def ingresarinsumos(request):
    producto = Productos.objects.all()

    data = {
        'from': ProductosFrom(),
        'producto':producto
    }
    
    if request.method == 'POST':
        fromulario = ProductosFrom(data=request.POST, files=request.FILES)
        if fromulario.is_valid():
            fromulario.save()
            messages.success(request, "insumo registrado")
            return redirect(to="listar-insumos" )
        else:
            data["from"] = fromulario

    return render(request, 'app/producto/ingresoInsumos.html', data)

@permission_required('app.view_productos')
def listar_Insumos(request):
    
    product = Productos.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(product, 10)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': product,
        'paginator': paginator
    }

    return render(request, 'app/producto/listarInsumos.html',data)

@permission_required('app.change_productos')
def modificar_Insumos(request, id):
    
    producto = get_object_or_404(Productos, id=id)

    data = {
        'from' : ProductosFrom(instance=producto)
    }

    if request.method == "POST":
        formulario = ProductosFrom(data=request.POST, instance=producto, files=request.FILES )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar-insumos")
        data["form"] = formulario
        
    return render(request, 'app/producto/modificarInsumos.html', data)

@permission_required('app.delete_productos')
def eliminar_Insumos(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar-insumos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)
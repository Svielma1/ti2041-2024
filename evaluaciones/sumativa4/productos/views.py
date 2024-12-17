from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.timezone import now
from django.http import JsonResponse
from datetime import datetime
from .utils import generar_token
from .forms import CrearProductoForm

from .models import Product, Brand, Category

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']

        user = authenticate(request, username=usuario, password=contrasena)

        if user is not None:
            login(request, user)
            token = generar_token(user)
            request.session['token'] = token
            session = request.session
            session['username'] = user.username
            session['login_time'] = now().strftime('%Y-%m-%d %H:%M:%S')
            session['is_admin_products'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()
            print(f"Sesión - Username: {session['username']}, Login Time: {session['login_time']}, Is Admin: {session['is_admin_products']}")
            
            return redirect('productos')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'index.html')


def log_out(request):
    logout(request)
    request.session.flush()
    return redirect('login')

@login_required
def productos(request):
    productos = Product.objects.all()
    token = request.session.get("token", "")

    username = request.session.get('username', 'Invitado')
    login_time = request.session.get('login_time', 'No disponible')
    is_admin = request.session.get('is_admin_products', False)


    actual_user = {
        'username': username,
        'login_time': login_time,
        'is_admin': is_admin
    }

    context = { 
        'products': productos, 
        'user': actual_user,
        'token': token
    }
    return render(request, 'productos.html', context)

def verificador_grupo(user):
    return user.groups.filter(name='ADMIN_PRODUCTS').exists()

@login_required
@user_passes_test(verificador_grupo, login_url='productos')
def registro(request):
    if not request.user.groups.filter(name='ADMIN_PRODUCTS').exists():
        messages.error(request, "No tienes permisos para registrar productos.")
        return redirect('index') 

    if request.method == "POST":
        form = CrearProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(productos)
    else:
        form = CrearProductoForm()
    return render(request, "registro.html", {"form": form})

@login_required
def resultado(request, code):
    producto = get_object_or_404(Product, code=code)
    return render(request, "resultado.html", {'producto': producto, "mensaje": "Producto registrado con exito"})

@login_required
def editar_producto(request, code):
    product = get_object_or_404(Product, code=code)
    if request.method == 'POST':
        form = CrearProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = CrearProductoForm(instance=product)
    return render(request, 'editar.html', {'form': form})
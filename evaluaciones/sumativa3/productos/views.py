from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.timezone import now
from datetime import datetime

from .models import Product, Brand, Category

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']

        print(f"Usuario ingresado: {usuario}, Contraseña ingresada: {contrasena}")

        user = authenticate(request, username=usuario, password=contrasena)

        if user is not None:
            login(request, user)

            session = request.session
            session['username'] = user.username
            session['login_time'] = now().strftime('%Y-%m-%d %H:%M:%S')
            session['is_admin_products'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()
            print(f"Sesión - Username: {session['username']}, Login Time: {session['login_time']}, Is Admin: {session['is_admin_products']}")
            
            return redirect('productos')
        else:
            return render(request, 'index.html', {'error': 'Credenciales incorrectas'})
            
    return render(request, 'index.html')


def log_out(request):   
    logout(request)
    request.session.flush()
    return redirect('login')

@login_required
def productos(request):
    all_products = Product.objects.all()

    username = request.session.get('username', 'Invitado')
    login_time = request.session.get('login_time', 'No disponible')
    is_admin = request.session.get('is_admin_products', False)

    actual_products = []
    for product in all_products:
        actual_product = {
            'code': product.code,
            'name': product.name,
            'price': product.price,
            'brand': product.brand,
            'category': product.category,
        }
        actual_products.append(actual_product)

    actual_user = {
        'username': username,
        'login_time': login_time,
        'is_admin': is_admin
    }

    context = { 'products': actual_products, 'user': actual_user}
    return render(request, 'productos.html', context)

def verificador_grupo(user):
    return user.groups.filter(name='ADMIN_PRODUCTS').exists()

@login_required
@user_passes_test(verificador_grupo, login_url='productos')
def registro(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        marca_id = request.POST.get("marca")
        categoria_id = request.POST.get("categoria")

        marca = Brand.objects.get(id_brand = marca_id)
        categoria = Category.objects.get(id_category = categoria_id)

        producto = Product(
            name = nombre,
            price = precio,
            brand = marca,
            category = categoria
        )
        try:
            producto.save()
        except:
            return render('registro.html')
        return redirect(resultado, code = producto.code)
    
    marcas = Brand.objects.all()
    categorias = Category.objects.all()
    return render(request, 'registro.html', {'marcas': marcas, 'categorias': categorias})

@login_required
def resultado(request, code):
    producto = get_object_or_404(Product, code=code)
    return render(request, "resultado.html", {'producto': producto, "mensaje": "Producto registrado con exito"})
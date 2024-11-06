from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from .models import Product, Brand, Category

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']

        user = authenticate(request, username=usuario, password=contrasena)

        if user is None:
            return HttpResponse('Error de autenticación', status=401)
        
        login(request, user=user)
        return redirect('productos')
    
    return render(request, 'index.html')

def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def productos(request):
    all_products = Product.objects.all()

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

    context = { 'products': actual_products}
    return render(request, 'productos.html', context)

@login_required
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
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Brand, Category

# Create your views here.
def index(request):
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
    return render(request, 'index.html', context)

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

    
def resultado(request, code):
    producto = get_object_or_404(Product, code=code)
    return render(request, "resultado.html", {'producto': producto, "mensaje": "Producto registrado con exito"})
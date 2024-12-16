from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate
from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404
from pydantic import ValidationError
from .models import Product, Brand, Category, Characteristics, Data
from .utils import generar_token, JWTAuth
from typing import List

api = NinjaAPI(
    title="API productos",
    description="Servicios para productos",
    version="1.0.0"
)

auth = JWTAuth()

# Manejadores de Errores
@api.exception_handler(Http404)
def error_404(request, ex):
    return api.create_response(request, 
                            {'response': 'Recurso no encontrado'},
                            status=404)
    
@api.exception_handler(ValidationError)
def error_validacion(request, ex):
    return api.create_response(request,
                            {
                                'response': 'Error de Formato de Entrada',
                                'errores': ex.errors()
                            },
                            status=422)

class AuthRequest(Schema):
    username: str
    password: str

@api.post(path="/token", tags=["Auth"])
def get_token(request, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return { "error": "Credenciales inválidas" }
    token = generar_token(user)
    return { "token": token }

@api.get(path="productos/", tags=["Products"])
def obtener_products(request):
    all_products = Product.objects.all().values()
    return list(all_products)

@api.get(path="productos/{code}", tags=["Products"])
def obtener_product(request, code: int):
    all_products = Product.objects.filter(code = code).values()
    return list(all_products)

class ProductSchema(Schema):
    name: str
    price: int
    brand: int
    category: int
    characteristics: List[int]

@api.post(path="productos/", auth=auth, tags=["Products"])
def add_products(request, data: ProductSchema):
    print(data)
    brand = Brand.objects.get(pk=data.brand)
    caterogy = Category.objects.get(pk=data.category)
    product = Product(
        name = data.name,
        price = data.price,
        brand = brand,
        category = caterogy
        
    )
    product.save()
    return {"name":product.name}

@api.put(path="productos/{code}", auth=auth, tags=["Products"])
def update_products(request, code: int, data: ProductSchema):
    product = get_object_or_404(Product, code=code)

    for attr, value in data.dict().items():
        if attr == "brand":
            value = get_object_or_404(Brand, id_brand=value)
        elif attr == "category":
            value = get_object_or_404(Category, id_category=value)
        elif attr == "characteristics":
            characteristics = [get_object_or_404(Characteristics, id=char_id) for char_id in value]
            product.characteristics.clear()
            for characteristic in characteristics:
                Data.objects.create(product=product, characteristics=characteristic)
            continue  
        setattr(product, attr, value)
    product.save()
    return { "code":product.code, "name":product.name }

@api.delete(path="productos/{code}", auth=auth, tags=["Products"])
def eliminar_producto(request, code: int):
    producto = Product.objects.filter(code=code).first()
    if not producto:
        raise Http404("Producto no encontrado")

    producto.delete()
    return {"message": "Producto eliminado exitosamente"}
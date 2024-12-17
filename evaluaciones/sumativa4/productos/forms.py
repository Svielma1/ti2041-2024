from django import forms
from .models import Product

class CrearProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "brand", "category"]
        labels = {
            "name": "Nombre del producto",
            "price": "Precio",
            "brand": "Marca",
            "category": "Categoría",
        }
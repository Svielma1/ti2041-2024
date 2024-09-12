from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        nombre = request.POST.get("nombre")
        marca = request.POST.get("marca")
        fecha_ven =request.POST.get("fecha_ven")
        if 'productos' not in request.session:
            request.session['productos'] = []

        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "marca": marca,
            "fecha_ven": fecha_ven
        }
        request.session['productos'].append(producto)
        request.session.modified = True
        return redirect(resultado)
    return render(request, 'registro.html')

    
def resultado(request):
    productos = request.session.get('productos')
    if not productos:
        return render(request, "resultado.html")
    producto = productos[-1]
    return render(request, "resultado.html", {'producto': producto, "mensaje": "Producto registrado con exito"})

def consulta(request):
    productos = request.session.get('productos', [])
    return render(request, 'consulta.html', {'productos': productos})
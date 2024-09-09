from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        context = {

            }
        return render(request, "registro.html", context)
    else:
        context = {

            }
        return render(request, "registro.html", context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from django.contrib.auth.views import logout_then_login


# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)



def home(request):
    return render(request, "index.html")

def listar(request):
    users = Usuarios.objects.all()
    datos = { "usuarios" : users }
    return render(request, "usuarios/listar.html", datos)

def agregar(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('f_nac'):
            user = Usuarios()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.save()
            return redirect("listar")
    else:
        return render(request, "usuarios/agregar.html")

def actualizar(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('f_nac'):
            user = Usuarios()
            user.id = request.POST.get('id')
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.save()
            return redirect("listar")
    else:
        users = Usuarios.objects.all()
        datos = { "usuarios" : users }
        return render(request, "usuarios/actualizar.html", datos)

def eliminar(request):
    return render(request, "usuarios/eliminar.html")

def logout(request):
    return logout_then_login(request, login_url="login")


def agregar_ropa(request):
    return render(request, "ropa/agregar_ropa.html")

def eliminar_ropa(request):
    return render(request, "ropa/eliminar_ropa.html")

def listar_ropa(request):
    return render(request, "ropa/listar_ropa.html")

def actualizar_ropa(request):
    return render(request, "ropa/actualizar_ropa.html")
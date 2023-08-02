from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

# Create your views here.
class InicioLoginView(LoginView):
    def get_success_url(self):
        return reverse('inicio')  # Importa reverse y reemplaza 'inicio' con el nombre de tu URL de inicio

login = InicioLoginView.as_view()


@login_required(login_url='/login/')
def inicio(request):
    usuario = request.user
    tiene_permiso_agregar = usuario.has_perm('vehiculo.add_vehiculo')
    tiene_permiso_visualizar = usuario.has_perm('vehiculo.visualizar_catalogo')

    context = {
        'tiene_permiso_agregar': tiene_permiso_agregar,
        'tiene_permiso_visualizar': tiene_permiso_visualizar,
    }
    return render(request, 'inicio.html', context)

def index(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos': vehiculos
    }
    return render(request, "index.html", context)

@login_required(login_url = "/login/")
@permission_required('vehiculo.add_vehiculo', login_url = "/login/")
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()

    context = {
        'form': form
    }
    return render(request, 'add.html', context)

@login_required(login_url = "/login/")
@permission_required('vehiculo.visualizar_catalogo', login_url = "/login/")
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos': vehiculos
    }
    return render(request, "listar.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    return render(request, 'logout.html')
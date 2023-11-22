from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductosFormulario, UserCreationFormCustom, UserEditForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin  # Nos obliga a tener un login


# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def nosotros(request):
    return render(request, "nosotros.html")


def productos_formulario(request):
    if request.method == "POST":
        mi_formulario = ProductosFormulario(request.POST, request.FILES)

        if mi_formulario.is_valid():
            mi_formulario.save()
            return render(request, "inicio.html")
    else:
        mi_formulario = ProductosFormulario()
    return render(request, "productos_formulario.html", {"mi_formulario": mi_formulario})


def buscador_precio(request):
    nombre_producto = request.GET.get('nombre',
                                      '')  # Aca con el metodo GET buscamos el valor de la clave "nombre" dentro del objeto request.
    precio_producto = None

    if nombre_producto:
        try:
            producto = Producto.objects.get(nombre=nombre_producto)
            precio_producto = producto.precio
        except Producto.DoesNotExist:
            precio_producto = "Producto no encontrado "

    formulario = ProductosFormulario()

    return render(request, 'buscador_precio.html',
                  {'formulario': formulario, 'nombre_producto': nombre_producto, 'precio_producto': precio_producto})


def leer_productos(request):
    productos = Producto.objects.all()
    return render(request, "leer_productos.html", {"productos": productos})


class ProductoListView(ListView):
    model = Producto
    context_object_name = "productos"
    template_name = "productos_lista.html"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos_detalle.html"


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "productos_crear.html"
    success_url = reverse_lazy("productos_lista")  # Es un redirect esto. Despues de darle submit y pasar datos, va ahi.
    fields = ["nombre", "marca", "descripcion", "precio", "imagen",
              "fechaPublicacion"]  # Le pasamos fields(campos) que queremos que se renderizen en el form del template.


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos_editar.html"
    fields = ["nombre", "marca", "descripcion", "precio", "imagen",
              "fechaPublicacion"]
    success_url = reverse_lazy('productos_lista')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos_borrar.html"
    success_url = reverse_lazy('productos_lista')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            login(request, user)
            return render(request, "inicio.html", {"mensaje": f"Bienvenido {user.username}"})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            form.save()
            return render(request, "inicio.html", {"mensaje": "Usuario creado"})
    else:
        form = UserCreationFormCustom
    return render(request, "registro.html", {"form": form})


def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid():
            avatar = getattr(usuario, 'avatar', None)
            if avatar:
                avatar.imagen = miFormulario.cleaned_data.get('imagen')
                avatar.save()
            miFormulario.save()
            return render(request, "inicio.html")
    else:
        avatar = getattr(usuario, 'avatar', None)
        initial_data = {'imagen': avatar.imagen if avatar else None}
        miFormulario = UserEditForm(initial=initial_data, instance=request.user)
    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


class Cambiar_Contrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "cambiar_contrasenia.html"
    success_url = reverse_lazy("editar_perfil")

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# Para las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("", views.inicio, name="inicio"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("productos_formulario/", views.productos_formulario, name="productos_formulario"),
    path('buscador_precio/', views.buscador_precio, name='buscador_precio'),
    path("leer_productos/", views.leer_productos, name="leer_productos"),
    path("producto/lista", views.ProductoListView.as_view(), name="productos_lista"),
    path("producto/nuevo", views.ProductoCreateView.as_view(), name="NuevoProducto"),
    path("producto/<pk>", views.ProductoDetailView.as_view(), name="DetalleProducto"),
    path("producto/<pk>/editar", views.ProductoUpdateView.as_view(), name="EditarProducto"),
    path("producto/<pk>/borrar", views.ProductoDeleteView.as_view(), name="BorrarProducto"),
    path("login", views.login_request, name="Login"),
    path("registro", views.register, name="Registro"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
    path("cambiar_contrasenia", views.Cambiar_Contrasenia.as_view(), name="cambiar_contrasenia"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

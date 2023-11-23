from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm
from .models import Producto


class ProductosFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'descripcion', 'precio', 'imagen', 'fechaPublicacion']


class UserCreationFormCustom(UserCreationForm):
    user = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    descripcion = forms.CharField(label="Descripcion")
    mas_info = forms.URLField(label="Link con mas info")

    class Meta:
        model = UserModel
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

    def __init__(self, *args, **kwargs):
        super(UserCreationFormCustom, self).__init__(*args, **kwargs)


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = UserModel
        fields = ["email", "last_name", "first_name", "imagen"]

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class ClienteFormulario(forms.Form):

       nombre = forms.CharField()
       apellido = forms.CharField()
       mail = forms.EmailField()
       usuario = forms.CharField()

class BusquedaFormulario(forms.Form):

       album = forms.CharField()
       artista = forms.CharField()
       año = forms.IntegerField()


class AgregarAlbum(forms.Form):

       album = forms.CharField()
       artista = forms.CharField()
       fechaLanzamiento = forms.IntegerField()
       genero = forms.CharField()
       subGenero = forms.CharField()
       formato = forms.CharField()
       paisOrigen = forms.CharField()
       disponibilidad = forms.BooleanField()
       codigo = forms.IntegerField()
       descripcion = forms.CharField()
       
class Suscripcion(forms.Form):

       mail = forms.EmailField()
       nombre = forms.CharField()

class RegistroUser(UserCreationForm):

       email = forms.EmailField()
       password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
       password2 = forms.CharField(label = "Volvé a escribir la contraseña", widget=forms.PasswordInput) 
       class Meta:
              model  = User
              fields = ['username', 'password1', 'password2', 'email','first_name', 'last_name']

class FormularioEditar(UserCreationForm):

       email = forms.EmailField()
       password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
       password2 = forms.CharField(label = "Volvé a escribir la contraseña", widget=forms.PasswordInput) 
       class Meta:
              model  = User
              fields = ['password1', 'password2', 'email','first_name', 'last_name']

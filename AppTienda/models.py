from django.db import models
from django.contrib.auth.models import User

class Tienda(models.Model):

       def __str__(self) -> str:
              return f"{self.id}. Album {self.album} de {self.artista} del año {self.fechaLanzamiento} | Formato: {self.formato} | Disponibilidad: {self.disponibilidad}"

       album = models.CharField(max_length=55)
       artista = models.CharField(max_length=55)
       fechaLanzamiento = models.IntegerField(blank=True)
       genero = models.CharField(max_length=55)
       subGenero = models.CharField(max_length=255)
       formato = models.CharField(max_length=55)
       paisOrigen = models.CharField(max_length=55)
       disponibilidad = models.BooleanField(blank=True)
       #precio = models.IntegerField(blank=True)
       codigo = models.IntegerField(help_text="Valor en ARS$") #Este es el precio
       descripcion = models.CharField(max_length=255)   

class Cliente(models.Model):

       def __str__(self) -> str:
              return f"{self.id}. Nick: >{self.usuario}< | Nombre y apellido: {self.nombre} {self.apellido} | Mail: {self.mail}"


       nombre = models.CharField(max_length=55)
       apellido = models.CharField(max_length=55)
       mail = models.EmailField(max_length=60)
       usuario = models.CharField(max_length=55)

class Contacto(models.Model):
       def __str__(self) -> str:
              return f'{self.id}. Nick: "{self.usuario}" | Datos: {self.nombre} {self.telefono} {self.mail}' 
       nombre = models.CharField(max_length=55)
       telefono = models.IntegerField(blank=True)
       mail = models.EmailField(max_length=60)
       usuario = models.CharField(max_length=55)

class Cotizar(models.Model):
       def __str__(self) -> str:
              return f'{self.id}. Album {self.album} de {self.artista} | Formato: {self.formato} | Descripcion: {self.descripcion} | Teléfono: {self.telefono}(preguntar por "{self.nombre}")'  
       album = models.CharField(max_length=55)
       artista = models.CharField(max_length=55)
       formato = models.CharField(max_length=55)
       descripcion = models.CharField(max_length=255)
       
       nombre = models.CharField(max_length=100)
       telefono = models.IntegerField(blank=True)
       mail = models.EmailField(max_length=60)

class Suscribete(models.Model):
       def __str__(self) -> str:
              return f'{self.id}. Nombre: {self.nombre} | Mail: {self.mail}'
       mail = models.EmailField(max_length=60)
       nombre = models.CharField(max_length=55)

class Preventa(models.Model):
       
       def __str__(self) -> str:
              return f'{self.id}. Album {self.album} de {self.artista} | Formato: {self.formato} | Descripcion: {self.descripcion} | Teléfono: {self.telefono}(preguntar por "{self.nombre}")'

       album = models.CharField(max_length=55)
       artista = models.CharField(max_length=55)
       formato = models.CharField(max_length=55)
       descripcion = models.CharField(max_length=255)       
       nombre = models.CharField(max_length=100)
       telefono = models.IntegerField(blank=True)
       mail = models.EmailField(max_length=60)

class AvatarImagen(models.Model):
       usuario = models.ForeignKey(User,on_delete=models.CASCADE)
       imagen = models.ImageField(upload_to="avatares",null=True, blank=True)
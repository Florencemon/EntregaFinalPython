from django.shortcuts import render
from django.http import HttpResponse
from AppTienda.models import *
from AppTienda.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



def inicio(request):
      return render(request, 'AppTienda/inicio.html')

def tienda(request):

      return render(request, 'AppTienda/tienda.html')
 
def cliente(request):
      return render(request, 'AppTienda/cliente.html')
      
def contacto(request):
      return render(request, 'AppTienda/contacto.html')

def cotizar(request):
      return render(request, 'AppTienda/cotizar.html')

def suscribete(request):
      return render(request, 'AppTienda/suscribete.html')

def preventa(request):
      return render(request, 'AppTienda/preventa.html')
      
def clienteFormulario(request):  #NUEVOCLIENTE  

      if request.method == 'POST':
            formulario1 = ClienteFormulario(request.POST)
            if formulario1.is_valid():
                  info = formulario1.cleaned_data

                  cliente = Cliente(nombre=info['nombre'], apellido=info['apellido'], mail=info['mail'], usuario=info['usuario'])
                  
                  cliente.save()
                  return render(request, 'Apptienda/inicio.html')

      else:

                  formulario1 = ClienteFormulario()

      return render(request, 'AppTienda/clienteFormulario.html', {"form1":formulario1})
def busquedaCliente(request):

      return render(request, 'AppTienda/inicio.html')
def resultadoCliente(request): #RESULTADOS

      if request.GET['nombre']:

            nombre = request.GET['nombre']
            usuario = Cliente.objects.filter(nombre__icontains=nombre)

            return render(request, "AppTienda/inicio.html", {"usuario":usuario, "nombre":nombre})
      else:
            respuesta = "No hay resultados."

      return HttpResponse(respuesta)
@login_required
def agregarAlbum(request):  #CREAR ÍTEM EN TIENDA  

      if request.method == 'POST':
            formulario2 = AgregarAlbum(request.POST)
            if formulario2.is_valid():
                  info = formulario2.cleaned_data

                  cliente = Tienda(album=info['album'], artista=info['artista'], fechaLanzamiento=info['fechaLanzamiento'], genero=info['genero'], subGenero=info['subGenero'], formato=info['formato'], paisOrigen=info['paisOrigen'], disponibilidad=info['disponibilidad'], codigo=info['codigo'])
                  
                  cliente.save()
                  return render(request, 'Apptienda/inicio.html')

      else:

                  formulario2 = AgregarAlbum()

      return render(request, 'AppTienda/agregarAlbum.html', {"form2":formulario2})
def resultadoBusqueda(request): #RESULTADOS

      if request.GET['artista']:

            artista = request.GET['artista']
            album = Tienda.objects.filter(artista__icontains=artista)

            return render(request, "AppTienda/resultadoBusqueda.html", {"album":album, "artista":artista})
      else:
            respuesta = "No hay resultados."

      return HttpResponse(respuesta)
def suscripcion(request):    #SUSCRIPCION AL NEWSLETTER

      if request.method == 'POST':
            formulario3 = Suscripcion(request.POST)
            if formulario3.is_valid():
                  info = formulario3.cleaned_data

                  client3 = Suscribete(mail=info['mail'], nombre=info['nombre'])
                  
                  client3.save()
                  return render(request, 'Apptienda/inicio.html')

      else:

                  formulario3 = Suscripcion()

      return render(request, 'AppTienda/suscribete.html', {"form3":formulario3})
def leerAlbum(request): #VER ÍTEMS DE LA TIENDA
      tienda = Tienda.objects.all()

      contexto = {"albms": tienda}
      return render(request, 'AppTienda/leerAlbum.html', contexto)
def eliminarAlbum(request, albumNombre): #ELIMINAR ÍTEMS DE LA TIENDA
      album = Tienda.objects.get(album=albumNombre)
      album.delete()

      album = Tienda.objects.all()
      contexto = {"albms": album}

      return render(request, 'Apptienda/leerAlbum.html', contexto)
def editarAlbum(request, albumNombre): #MODIFICAR ÍTEMS DE LA TIENDA
      item = Tienda.objects.get(album=albumNombre)
      if request.method == 'POST':
            formulario2 = AgregarAlbum(request.POST)
            if formulario2.is_valid():
                  info = formulario2.cleaned_data
                  
                  item.album = info["album"]
                  item.artista = info["artista"]
                  item.fechaLanzamiento = info["fechaLanzamiento"]
                  item.genero = info["genero"]
                  item.subGenero = info["subGenero"] 
                  item.formato = info["formato"]
                  item.disponibilidad = info["disponibilidad"]
                  item.codigo = info["codigo"]
                  item.descripcion = info["descripcion"]


                  item.save()
                  return render(request, 'Apptienda/leerAlbum.html')

      else:

                  formulario2 = AgregarAlbum(initial={
                        "album":item.album,
                        "artista":item.artista,
                        "fechaLanzamiento":item.fechaLanzamiento,
                        "genero":item.genero,
                        "subGenero":item.subGenero,
                        "formato":item.formato,
                        "disponibilidad":item.disponibilidad,
                        "codigo":item.codigo,
                        "descripcion":item.descripcion} )

      return render(request, 'AppTienda/editarAlbum.html', {"form2":formulario2, "nombre": albumNombre})    
def log(request): #INICIAR SESIÓN
      if request.method== "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  user = form.cleaned_data.get('username')
                  pswrd = form.cleaned_data.get('password')  

                  usuario = authenticate(username = user, password = pswrd)
                  if usuario:
                        login(request, usuario)
                        return render(request, "AppTienda/inicio.html", {"mensaje":f"Hola, {usuario}"})

            else:
                  return render(request, "AppTienda/inicio.html", {"mensaje":"Datos incorrectos."}) 

      else:
            form = AuthenticationForm()
      return render(request, "AppTienda/login.html", {"formulario": form})
def registro(request):
      if request.method == "POST":
            form = RegistroUser(request.POST)

            if form.is_valid():
                  username = form.cleaned_data["username"]
                  form.save()
                  return render(request,"AppTienda/inicio.html", {"mensaje":"Usuario registrado correctamente."})

      else:
            form = RegistroUser()

      return render(request,"AppTienda/registro.html", {"formulario":form})

def editarUsuario(request):
      username = request.user
      if request.method == "POST":
            form = FormularioEditar(request.POST)

            if form.is_valid():
                  info = form.cleaned_data

                  username.email = info["email"]
                  username.set_password = info["password1"]
                  username.first_name = info["first_name"]
                  username.last_name = info["last_name"]

                  username.save()

                  return render(request, "AppTienda/inicio.html")

      else:
            form = FormularioEditar(initial={
                  "email":username.email,
                  "first_name":username.first_name,
                  "last_name":username.last_name,
            })

      return render(request, "AppTienda/editarPerfil.html", {"formulario":form, "username":username})

def acercaDe(request):
      return render(request, "AppTienda/staff.html", {"mensaje":"Quienes integramos el equipo de Flojosa Records Store"})

def busquedaAlbum(request):

      return render(request, 'AppTienda/resultadoBusqueda.html')
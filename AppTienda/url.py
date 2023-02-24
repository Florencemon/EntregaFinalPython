
from django.urls import path
from AppTienda.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('tienda', tienda, name='tienda'),
    path('cliente', cliente, name='cliente'),
    path('contacto', contacto, name='contacto'),
    path('cotizar/', cotizar, name='cotizar'),
    path('suscribete/', suscribete, name='suscribete'),
    path('preventa', preventa, name='preventa'),
    path('clienteFormulario/', clienteFormulario, name='clienteFormulario'),
    path('busquedaCliente', busquedaCliente, name="busquedaCliente"),
    path('resultadoCliente/',resultadoCliente, name="resultadoCliente"),
    path('agregarAlbum/',agregarAlbum, name="agregarAlbum"),
    path('resultadoBusqueda/',resultadoBusqueda, name="ResultadoBusqueda"),
    path('suscripcion/',suscripcion, name="suscripcion"),
    path('login/', log, name='Login'), #inicio de sesion
    path('registro/', registro, name='Registro'), 
    path('logout/', LogoutView.as_view(template_name="Apptienda/logout.html"), name="Logout"),
    path('editar/', editarUsuario, name="EditarUsuario"),
    path('staff/', acercaDe, name="Staff"),
    path('busquedaAlbum', busquedaAlbum, name="busquedaAlbum"),


    #CRUD de tienda:
    path('leerAlbum/',leerAlbum, name="leerAlbum"),
    path('eliminarAlbum/<albumNombre>',eliminarAlbum, name="albumEliminar"),
    path('editarAlbum/<albumNombre>',editarAlbum, name="editarAlbum"),
]
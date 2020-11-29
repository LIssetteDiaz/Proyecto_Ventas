"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from almacen import views, static
from almacen.views import ProductoListado, ProductoDetalle, ProductoCrear, ProductoActualizar, ProductoEliminar, ProductoDetalle2
from almacen.views import PagoListado, PagoDetalle, PagoCrear, PagoActualizar, PagoEliminar
from almacen.views import SucursalCrear, SucursalListado, SucursalDetalle, SucursalActualizar, SucursalEliminar
from almacen.views import CategoriaCrear, CategoriaListado, CategoriaDetalle, CategoriaActualizar, CategoriaEliminar
from almacen.views import TipoProductoCrear, TipoProductoListado, TipoProductoDetalle, TipoProductoActualizar, TipoProductoEliminar
from almacen.views import UsuarioListado, UsuarioDetalle, UsuarioCrear, UsuarioActualizar, UsuarioEliminar

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from rest_framework import routers

from almacen.views import ProductoList
router = routers.DefaultRouter()
router.register('productoRest',ProductoList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('venta/compra/', views.compra, name="compra"),
    path('venta/', views.venta, name="venta"),
    path('venta/<int:tipo>', views.venta, name="venta"),
    # path('venta/<int:tipo>/<str:docu>', views.venta, name="ventaCompra"),
    path('locales/', views.locales, name="locales"),
    # path('venta/detallesProducto/<int:producto>', views.DetallesProducto, name="detalleProducto"),
    path('indexadmin/', views.indexadmin, name="indexadmin"),
    path('empleados/', views.empleados, name="empleados"),
    
    path('registrar/', views.registrar, name="registrar"),
    path('ingresar/', views.ingresar, name="ingresar"),
    path('ingresoRequerido/', views.ingreso_requerido, name="ingresoRequerido"),
    path('salir/', views.cerrar_seccion, name="salir"),
   

    path('accounts/', include('django.contrib.auth.urls')),

    #************RestFull
    path('api/', include(router.urls)),
   
    #*********************

    #*********************IntegracionConFacebook
    path('oauth/', include('social_django.urls', namespace='social')),

    #******************************Restaurar contrasena
    path('reset_password/', 
        PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', 
        PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', 
        PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
    #**************************************************
    path('venta/detalle/<int:pk>', ProductoDetalle2.as_view(template_name = "detalleProducto.html"), name="detalleProducto"),
    #**************************************Producto
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('producto/', ProductoListado.as_view(template_name = "productos/producto.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('producto/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "productos/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('producto/crear', ProductoCrear.as_view(template_name = "productos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('producto/editar/<int:pk>', ProductoActualizar.as_view(template_name = "productos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('producto/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminar'),    
    #**************************************

    #**************************************Pago
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('pago/', PagoListado.as_view(template_name = "pago/pago.html"), name='leer_pago'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('pago/detalle/<int:pk>', PagoDetalle.as_view(template_name = "pago/detalles.html"), name='detalles_pago'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('pago/crear', PagoCrear.as_view(template_name = "pago/crear.html"), name='crear_pago'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('pago/editar/<int:pk>', PagoActualizar.as_view(template_name = "pago/actualizar.html"), name='actualizar_pago'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('pago/eliminar/<int:pk>', PagoEliminar.as_view(), name='eliminar_pago'),    
    #**************************************

    #**************************************Sucursal
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('sucursal/', SucursalListado.as_view(template_name = "sucursales/sucursal.html"), name='leerSucursal'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('sucursal/detalle/<int:pk>', SucursalDetalle.as_view(template_name = "sucursales/detalles.html"), name='detalles'),
    
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('sucursal/crear/', SucursalCrear.as_view(template_name = "sucursales/crear.html"), name='crearSuc'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('sucursal/editar/<int:pk>', SucursalActualizar.as_view(template_name = "sucursales/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('sucursal/eliminar/<int:pk>', SucursalEliminar.as_view(), name='eliminar'),    
    #**************************************

    # **************************************Categoria
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
     path('categoria/', CategoriaListado.as_view(template_name = "categorias/categoria.html"), name='leerCategoria'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
     path('categoria/detalle/<int:pk>', CategoriaDetalle.as_view(template_name = "categorias/detalles.html"), name='detalles'),
    
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
     path('categoria/crear/', CategoriaCrear.as_view(template_name = "categorias/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
     path('categoria/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "categorias/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
     path('categoria/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='eliminar'),    
    # **************************************

    # **************************************TipoProducto
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
     path('tipoProducto/', TipoProductoListado.as_view(template_name = "tiposProductos/tipoProducto.html"), name='leerTipoProducto'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
     path('tipoProducto/detalle/<int:pk>', TipoProductoDetalle.as_view(template_name = "tiposProductos/detalles.html"), name='detalles'),
    
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
     path('tipoProducto/crear/', TipoProductoCrear.as_view(template_name = "tiposProductos/crear.html"), name='crear_tipo'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
     path('tipoProducto/editar/<int:pk>', TipoProductoActualizar.as_view(template_name = "tiposProductos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
     path('tipoProducto/eliminar/<int:pk>', TipoProductoEliminar.as_view(), name='eliminar'),    
    # **************************************

    # **************************************Usuario
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
     path('usuarioAdmin/', UsuarioListado.as_view(template_name = "administrar_usuarios/usuarioAdmin.html"), name='leerUsuario'),
 
    # # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
     path('usuarioAdmin/detalle/<int:pk>', UsuarioDetalle.as_view(template_name = "administrar_usuarios/detalles.html"), name='detalles'),
    
 
    # # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    #  path('usuarioAdmin/crear/', UsuarioCrear.as_view(template_name = "administrar_usuarios/crear.html"), name='crear'),
    path('usuarioAdmin/crear/', views.UsuarioCrear, name="crearUsuarioAdmin"),
    # # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('usuarioAdmin/editar/<int:id>', views.UsuarioActualizar, name="editarUsuarioAdmin"),
 
    # # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
     path('usuarioAdmin/eliminar/<int:pk>', UsuarioEliminar.as_view(), name='eliminar'),    
    # # **************************************
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL = '/'
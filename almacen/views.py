from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms
from almacen.forms import FormSucursales, FormTipoProducto, FormProducto, FormRegistro, FormIngreso

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import PRODUCTO, CATEGORIA, TIPO_PRODUCTO, FORMA_PAGO, SUCURSAL, DOCUMENTO
from django.contrib.auth.models import User

from .serializers import ProductoSerializer
from rest_framework import viewsets

class ProductoList(viewsets.ModelViewSet):
    queryset = FORMA_PAGO.objects.all()
    serializer_class = ProductoSerializer


# class ProgrammerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CATEGORIA.objects.all()
#     serializer_class = ProgrammerSerializer

def index(request):
    return render(request, 'index.html')

@login_required(login_url="ingresoRequerido")
def compra(request):
    return render(request, 'compra.html')

def venta(request, tipo = None):
    if tipo is not None:
        prod = PRODUCTO.objects.filter(tipo_producto=tipo)
    else:
        prod = PRODUCTO.objects.all()


    if request.method == 'POST':
        
        descDocu = request.POST['descDocu']

        documento = DOCUMENTO(
            descripcion = descDocu
        )

        documento.save()

    categ = CATEGORIA.objects.all()
    
    tipo = TIPO_PRODUCTO.objects.all()

    product = list(prod.values())
    cantidad = PRODUCTO.objects.count()
    # producto.objects.raw("aqui va consulta sql")
    return render(request, 'venta.html',{
    'productos': product,
    'cant': cantidad,
    'categorias': categ,
    'tipo': tipo,
    })

# def DetallesProducto(request, producto = None):
#     prod = PRODUCTO.objects.filter(id = producto)

#     return render(request, 'detalleProducto.html', {'prod': prod})

def locales(request):
    sucursales = SUCURSAL.objects.all()
    return render(request, 'locales.html',{'sucursales':sucursales})

def registrar(request):

    form = FormRegistro()
    email = request.POST.get('email')
    validarEmail = User.objects.filter(email = email)

    
    if request.method == 'POST':
        if validarEmail:
            messages.warning(request, 'el email ya existe')
        else:
            form = FormRegistro(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
    
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    return render(request, 'usuarios/registro.html',{'form':form})

def ingresar(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'f')
        
    return render(request, 'usuarios/ingreso.html')

def ingreso_requerido(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('../venta/compra/')
        else:
            messages.warning(request, 'f')
        
    return render(request, 'usuarios/ingresoRequerido.html')

def cerrar_seccion(request):
    logout(request)
    return redirect('/')

def indexadmin(request):
    return render(request, 'indexadmin.html')

def producto(request):
    return render(request, 'producto.html')

def empleados(request):
    return render(request, 'empleados.html')


# *****************************************************CrudProducto******************************************************************
class ProductoListado(ListView): 
    model = PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class ProductoCrear(SuccessMessageMixin, CreateView, ListView): 
    model = PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = FormProducto() # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
   
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ProductoDetalle(DetailView): 
    model = PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = FormProducto() # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = PRODUCTO 
    form = FormProducto()
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
# *****************************************************finCrudProducto******************************************************************


# *****************************************************CrudPago******************************************************************
class PagoListado(ListView): 
    model = FORMA_PAGO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class PagoCrear(SuccessMessageMixin, CreateView): 
    model = FORMA_PAGO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = FORMA_PAGO # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'FORMA PAGO Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer_pago') # Redireccionamos a la vista principal 'leer'

class PagoDetalle(DetailView): 
    model = FORMA_PAGO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class PagoActualizar(SuccessMessageMixin, UpdateView): 
    model = FORMA_PAGO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = FORMA_PAGO # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'FORMA PAGO Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer_pago') # Redireccionamos a la vista principal 'leer'

class PagoEliminar(SuccessMessageMixin, DeleteView): 
    model = FORMA_PAGO 
    form = FORMA_PAGO
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'FORMA_PAGO Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer_pago') # Redireccionamos a la vista principal 'leer'

# ***************************************************finCrudPago**********************************************************


# *****************************************************CrudSucursales******************************************************************
class SucursalListado(ListView): 
    model = SUCURSAL # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class SucursalCrear(SuccessMessageMixin, CreateView, ListView): 
    model = SUCURSAL # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = FormSucursales() # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Sucursal Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerSucursal') # Redireccionamos a la vista principal 'leer'

class SucursalDetalle(DetailView): 
    model = SUCURSAL # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class SucursalActualizar(SuccessMessageMixin, UpdateView): 
    model = SUCURSAL # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = FormSucursales() # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Sucursal Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerSucursal') # Redireccionamos a la vista principal 'leer'

class SucursalEliminar(SuccessMessageMixin, DeleteView): 
    model = SUCURSAL 
    form = FormSucursales()
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Sucursal Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerSucursal') # Redireccionamos a la vista principal 'leer'
# *****************************************************finCrudSucursales****************************************************************



# *****************************************************CrudCategoria******************************************************************
class CategoriaListado(ListView): 
    model = CATEGORIA # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class CategoriaCrear(SuccessMessageMixin, CreateView, ListView): 
    model = CATEGORIA # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = CATEGORIA # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCategoria') # Redireccionamos a la vista principal 'leer'

class CategoriaDetalle(DetailView): 
    model = CATEGORIA # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class CategoriaActualizar(SuccessMessageMixin, UpdateView): 
    model = CATEGORIA # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = CATEGORIA # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCategoria') # Redireccionamos a la vista principal 'leer'

class CategoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = CATEGORIA 
    form = CATEGORIA
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoria') # Redireccionamos a la vista principal 'leer'
# *****************************************************finCrudCategoria****************************************************************

# *****************************************************CrudTipoProducto******************************************************************
class TipoProductoListado(ListView): 
    model = TIPO_PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class TipoProductoCrear(SuccessMessageMixin, CreateView, ListView): 
    model = TIPO_PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = FormTipoProducto() # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerTipoProducto') # Redireccionamos a la vista principal 'leer'

class TipoProductoDetalle(DetailView): 
    model = TIPO_PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class TipoProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = TIPO_PRODUCTO # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = FormTipoProducto() # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerTipoProducto') # Redireccionamos a la vista principal 'leer'

class TipoProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = TIPO_PRODUCTO 
    form = FormTipoProducto()
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerTipoProducto') # Redireccionamos a la vista principal 'leer'
# *****************************************************finCrudCategoria****************************************************************

# *****************************************************CrudUsuarios******************************************************************
class UsuarioListado(ListView): 
    model = User # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class UsuarioCrear(SuccessMessageMixin, CreateView, ListView): 
    model = User # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = User # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Usuario Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
    
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerUsuario') # Redireccionamos a la vista principal 'leer'

class UsuarioDetalle(DetailView): 
    model = User # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'

class UsuarioActualizar(SuccessMessageMixin, UpdateView): 
    model = User # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = User # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Usuario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerUsuario') # Redireccionamos a la vista principal 'leer'

class UsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = User 
    form = User
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerUsuario') # Redireccionamos a la vista principal 'leer'
# *****************************************************finCrudUsuarios******************************************************************

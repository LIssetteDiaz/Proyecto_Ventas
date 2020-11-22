from django import forms
from .models import SUCURSAL, TIPO_PRODUCTO, PRODUCTO
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormSucursales(forms.ModelForm):

    # def __init__(self,*args,**kwargs):
    #     super(FormSucursales,self).__init__(*args,**kwargs)
    #     for i in self.visible_fields():
    #         i.field.widget.attrs["class"]="form-control"
    # nombre = forms.CharField(
    #     label = "Nombre"
    # )

    # descripcion = forms.CharField(
    #     label = "Descripcion",
    #     widget = forms.Textarea
    # )

    # direccion = forms.CharField(
    #     label = "Direccion"
    # )

    # imagen = forms.ImageField(
    #     label = "Imagen"
    # )


    class Meta:
        model = SUCURSAL
        fields = ("nombre","descripcion","direccion","imagen","comuna")
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        }


class FormTipoProducto(forms.ModelForm):

    class Meta:
        model = TIPO_PRODUCTO
        fields = ("nombre","categoria")
        
class FormProducto(forms.ModelForm):

    class Meta:
        model = PRODUCTO
        fields = ("codigo_barra","nombre","descripcion","stock","precio_venta", "precio_compra","imagen","tipo_producto")
        
class FormRegistro(UserCreationForm):
    
    def __init__(self,*args,**kwargs):
        super(FormRegistro,self).__init__(*args,**kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs["class"]="form-control"
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","password1","password2")
       
class FormIngreso(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(FormIngreso,self).__init__(*args,**kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs["class"]="form-control"
    class Meta:
        model = User
        fields = ("email","password1")
from django.db import models

class DOCUMENTO(models.Model):
    descripcion = models.CharField(max_length=200, default=None)

class FORMA_PAGO(models.Model):
    descripcion = models.CharField(max_length=200, default=None)

class VENTA(models.Model):
    total = models.IntegerField(default=None)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    documento = models.ForeignKey(DOCUMENTO,on_delete=models.CASCADE,default=None)
    forma_pago = models.ForeignKey(FORMA_PAGO,on_delete=models.CASCADE,default=None)
    #usuario = models.ForeignKey(USUARIO,on_delete=models.CASCADE,default=0)

class REGION(models.Model):
    nombre = models.CharField(max_length=200, default=None)
    numeracion = models.CharField(max_length=200, default=None)

class LOCALIDAD(models.Model):
    nombre = models.CharField(max_length=200, default=None)
    region = models.ForeignKey(REGION,on_delete=models.CASCADE,default=None)

class COMUNA(models.Model):
    nombre = models.CharField(max_length=200, default=None)
    localidad = models.ForeignKey(LOCALIDAD,on_delete=models.CASCADE,default=None)
    
    def  __str__(self):
        return self.nombre
    

class ENTREGA(models.Model):
    email = models.EmailField(default=None)
    direccion = models.CharField(max_length=100, default=None)
    comuna = models.ForeignKey(COMUNA,on_delete=models.CASCADE,default=None)
    venta = models.ForeignKey(VENTA,on_delete=models.CASCADE,default=None)

class CATEGORIA(models.Model):
    nombre = models.CharField(max_length=200, default=None)
    def  __str__(self):
        return self.nombre
    
class TIPO_PRODUCTO(models.Model):
    nombre = models.CharField(max_length=200, default=None)
    categoria = models.ForeignKey(CATEGORIA,on_delete=models.CASCADE,default=None)
    def  __str__(self):
        return self.nombre
    

class PRODUCTO(models.Model):
    codigo_barra = models.IntegerField(default=None)
    nombre = models.CharField(max_length=200, default=None)
    descripcion = models.CharField(max_length=200, default=None)
    stock = models.IntegerField(default=None)
    precio_venta = models.IntegerField(default=None)
    precio_compra = models.IntegerField(default=None)
    imagen = models.ImageField(default=None,upload_to="productos")
    tipo_producto = models.ForeignKey(TIPO_PRODUCTO,on_delete=models.CASCADE,default=None)

class SUCURSAL(models.Model):
    nombre = models.CharField(max_length=200, default=None)
    descripcion = models.TextField(max_length=200, default=None)
    direccion = models.CharField(max_length=200, default=None)
    imagen = models.FileField(max_length=200, default=None)
    comuna = models.ForeignKey(COMUNA,on_delete=models.CASCADE,default=None)


class DETALLE(models.Model):
    cantidad = models.IntegerField(default=None)
    venta = models.ForeignKey(VENTA,on_delete=models.CASCADE,default=None)
    producto = models.ForeignKey(PRODUCTO,on_delete=models.CASCADE,default=None)
    sucursal = models.ForeignKey(SUCURSAL,on_delete=models.CASCADE,default=None)

#importar datetime   
#end_date = models.DateTimeField(auto_now_add=True)



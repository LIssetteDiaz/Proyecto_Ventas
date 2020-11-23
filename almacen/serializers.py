from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import PRODUCTO, FORMA_PAGO

# class ProductoSerializer(serializers.Serializer):
#     codigo_barra = serializers.IntegerField()
#     nombre = serializers.CharField()
#     descripcion = serializers.CharField()
#     stock = serializers.IntegerField()
#     precio_venta = serializers.IntegerField()
#     precio_compra = serializers.IntegerField()
#     imagen = serializers.CharField()
#     tipo_producto = serializers.CharField()

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FORMA_PAGO
        fields = ("__all__")

# def create(self, validated_data):
#     """
#     Create and return a new Serie instance, given the validated data.
#     """
#     return PRODUCTO.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     """
#     Update and return an existing Serie instance, given the validated data.
#     """
#     instance.codigo_barra = validated_data.get('codigo_barra', instance.codigo_barra)
#     instance.nombre = validated_data.get('nombre', instance.nombre)
#     instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#     instance.stock = validated_data.get('stock', instance.stock)
#     instance.precio_venta = validated_data.get('precio_venta', instance.precio_venta)
#     instance.precio_compra =  validated_data.get('precio_compra', instance.precio_compra)
#     instance.imagen = validated_data.get('imagen', instance.imagen)
#     instance.tipo_producto = validated_data.get('tipo_producto', instance.tipo_producto)
#     instance.save()
#     return instance



# {
#     "codigo_barra":500000, 
#     "nombre": "pruebajson", 
#     "descripcion": "pruebajson", 
#     "stock":10, 
#     "precio_venta":2000, 
#     "precio_compra":1500, 
#     "imagen": "productos/chorizo.jpg", 
#     "tipo_producto": "Congelados"
# }



# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def init(self, data, kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).init(content, kwargs)

# @csrf_exempt
# def ProductoLista(request):
#     """
#     List all code serie, or create a new serie.
#     """
#     if request.method == 'GET':
#         producto = PRODUCTO.objects.all()
#         serializer = ProductoSerializer(producto, many=True)
#         return JSONResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         producto = ProductoSerializer(data=data)
#         if producto.is_valid():
#             producto.save()
#             return JSONResponse(producto.data, status=201)
#         return JSONResponse(producto.errors, status=400)

# @csrf_exempt
# def ProductoDetalle(request, pk):
#     """
#     Retrieve, update or delete a serie.
#     """
#     try:
#         producto = PRODUCTO.objects.get(pk=pk)
#     except PRODUCTO.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         producto = ProductoSerializer(producto)
#         return JSONResponse(producto.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         producto = ProductoSerializer(producto, data=data)
#         if producto.is_valid():
#             producto.save()
#             return JSONResponse(producto.data)
#         return JSONResponse(producto.errors, status=400)

#     elif request.method == 'DELETE':
#         producto.delete()
#         return HttpResponse(status=204)
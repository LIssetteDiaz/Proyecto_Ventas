from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import PRODUCTO, FORMA_PAGO


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FORMA_PAGO
        fields = ("__all__")


# {
#     "descripcion": "prueba"
# }



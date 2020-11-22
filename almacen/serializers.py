from rest_framework import serializers
from .models import FORMA_PAGO


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FORMA_PAGO
        fields = ("__all__")
    

    
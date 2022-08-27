from dataclasses import field, fields
from rest_framework import serializer

from tarjetas.models import Tarjeta
from prestamos.models import Prestamo
from cliente.models import Cliente 
from cuentas.models import Cuenta


class clienteSerializer(serializer.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = "__all__"
        read_only_fields = ("customers_id")


class tarjetaSerializer(serializer.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"

class prestamoSerializer(serializer.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"
        
class cuentaSerializer(serializer.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"
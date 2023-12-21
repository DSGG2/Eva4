from rest_framework import serializers
from .models import Empresa, Personal, Transporte

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id','nombre','litros','tamano','precio','proveedor','tipoagua')
        

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('id','nombre','cargo','edad','experiencia','telefono','email')

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = ('id','nombre','modelo','capacidad','fecha_fabricacion','estado','costo_mantenimiento')

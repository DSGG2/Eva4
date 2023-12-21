from rest_framework import viewsets
from .models import Empresa, Personal, Transporte
from .serializers import EmpresaSerializer, PersonalSerializer, TransporteSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class TransporteViewSet(viewsets.ModelViewSet):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer


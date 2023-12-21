from django.db import models

class Empresa(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    nombre =models.CharField(max_length=255),
    litros = models.IntegerField(),
    tamano =models.CharField(max_length=50),
    precio= models.DecimalField(decimal_places=2, max_digits=10),
    proveedor=models.CharField(max_length=255),
    tipoagua= models.CharField(choices=[('A', 'Agua Purificada'), ('B', 'Otro Tipo')], max_length=1),

class Personal(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    nombre= models.CharField(max_length=255),
    cargo= models.CharField(max_length=100),
    edad =models.IntegerField(),
    experiencia= models.IntegerField(),
    telefono= models.CharField(max_length=15),
    email= models.EmailField(max_length=254),
    
class Transporte(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    nombre= models.CharField(max_length=255),
    modelo= models.CharField(max_length=100),
    capacidad= models.IntegerField(),
    fecha_fabricacion= models.DateField(),
    estado= models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], max_length=1),
    costo_mantenimiento= models.DecimalField(decimal_places=2, max_digits=10),
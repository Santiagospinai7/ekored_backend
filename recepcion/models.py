from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tblEKOProveedores(models.Model):
  id_fiscal = models.CharField(max_length=20, primary_key=True)
  id_acopio = models.ForeignKey('tblEKOAcopio', on_delete=models.CASCADE)

  compania = models.CharField(max_length=250)
  razon_social = models.CharField(max_length=500)
  nombre_comercial = models.CharField(max_length=500)
  codigo_JDE = models.IntegerField()
  codigo_siesa = models.IntegerField()
  tipo_contribuyente = models.CharField(max_length=10)
  celular = models.CharField(max_length=15)
  correo = models.CharField(max_length=15)
  codigo_postal = models.CharField(max_length=15)

  codigo_JDE_padre = models.IntegerField()
  tipo = models.CharField(max_length=30)

  cod_categoria_1 = models.CharField(max_length=25)
  cod_categoria_2 = models.CharField(max_length=25)
  cod_categoria_3 = models.CharField(max_length=25)
  cod_categoria_4 = models.CharField(max_length=25)
  cod_categoria_5 = models.CharField(max_length=25)
  cod_categoria_6 = models.CharField(max_length=25)
  cod_categoria_7 = models.CharField(max_length=25)
  cod_categoria_8 = models.CharField(max_length=25)
  cod_categoria_9 = models.CharField(max_length=25)
  cod_categoria_10 = models.CharField(max_length=25)

  activo = models.BooleanField()

  def __str__(self):
      return self.id_fiscal  # Display ifFiscal as the string representation of the object

class tblEKOAcopio(models.Model):
  cod_acopio = models.CharField(max_length=20, unique=True)

  nombre = models.CharField(max_length=100)
  cod_categoria_1 = models.CharField(max_length=25)
  cod_categoria_2 = models.CharField(max_length=25)
  cod_categoria_3 = models.CharField(max_length=25)
  cod_categoria_4 = models.CharField(max_length=25)
  cod_categoria_5 = models.CharField(max_length=25)

  cod_ciudad = models.CharField(max_length=20)

  def __str__(self):
    return self.cod_acopio

class tblEKOTicket(models.Model):
  id_acopio = models.ForeignKey('tblEKOAcopio', on_delete=models.CASCADE)
  cod_zona = models.ForeignKey('tblEKOZona', on_delete=models.CASCADE)

  fecha = models.DateField()
  proveedor = models.ForeignKey('tblEKOProveedores', on_delete=models.CASCADE)
  proveedor_padre = models.CharField(max_length=30)
  tipo = models.CharField(max_length=30)

  placa = models.CharField(max_length=10)
  nombre_transportador = models.CharField(max_length=60)
  nro_remision = models.CharField(max_length=20)
  peso_remision = models.DecimalField(max_digits=10, decimal_places=2)

  estado = models.FloatField()
  usuario_ingreso = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingreso_tickets')
  usuario_validacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name='validacion_tickets')
  fecha_validacion = models.DateField()

  def __str__(self):
    return f"{self.id_acopio} - {self.fecha}"

class tblEKOZona(models.Model):
  cod_zona = models.CharField(max_length=20, primary_key=True)
  zona = models.CharField(max_length=100)

  cod_categoria_1 = models.CharField(max_length=25)
  cod_categoria_2 = models.CharField(max_length=25)
  cod_categoria_3 = models.CharField(max_length=25)
  cod_categoria_4 = models.CharField(max_length=25)
  cod_categoria_5 = models.CharField(max_length=25)

  def __str__(self):
    return self.cod_zona

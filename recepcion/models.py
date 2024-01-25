from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Acopio(models.Model):
  class Meta:
    db_table = '[transversal].[tblEkoAcopios]'
  cod_acopio = models.CharField(max_length=20, unique=True)

  nombre = models.CharField(max_length=100)
  cod_categoria_1 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_2 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_3 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_4 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_5 = models.CharField(max_length=25, null=True, blank=True)

  cod_ciudad = models.CharField(max_length=20)

  def __str__(self):
    return self.cod_acopio

class Proveedor(models.Model):
  class Meta:
    db_table = '[transversal].[tblEkoProveedores]'

  id_fiscal = models.CharField(max_length=20, primary_key=True)
  id_acopio = models.ForeignKey(Acopio, on_delete=models.CASCADE)

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



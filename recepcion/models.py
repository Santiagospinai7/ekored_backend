from django.db import models
import uuid
# from django.contrib.auth.models import User

# Create your models here.
class Acopio(models.Model):
  class Meta:
    db_table = '[transversal].[tblEkoAcopios]'

  id_acopio = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
    unique=True
  )
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

  uuid = models.UUIDField( 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        ) 
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

class Zona(models.Model):
  class Meta:
    db_table = '[recepcion].[tblEKOZonas]'

  uuid = models.UUIDField( 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        ) 
  cod_zona = models.CharField(max_length=20, primary_key=True)
  zona = models.CharField(max_length=100)

  cod_categoria_1 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_2 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_3 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_4 = models.CharField(max_length=25, null=True, blank=True)
  cod_categoria_5 = models.CharField(max_length=25, null=True, blank=True)

  def __str__(self):
    return self.cod_zona

class Ticket(models.Model):
  class Meta:
    db_table = '[recepcion].[tblEKOTickets]'

  id_ticket = models.UUIDField(
          primary_key = True, 
          default = uuid.uuid4,
          editable = False, 
          unique=True
          ) 
  id_acopio = models.ForeignKey(Acopio, on_delete=models.CASCADE)
  cod_zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

  fecha = models.DateField()
  proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
  proveedor_padre = models.CharField(max_length=30)
  tipo = models.CharField(max_length=30)

  placa = models.CharField(max_length=10)
  nombre_transportador = models.CharField(max_length=60)
  nro_remision = models.CharField(max_length=20)
  peso_remision = models.DecimalField(max_digits=10, decimal_places=2)

  estado = models.FloatField()
  # usuario_ingreso = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingreso_tickets')
  # usuario_validacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name='validacion_tickets')
  fecha_validacion = models.DateField()

  def __str__(self):
    return self.id_ticket

class Localizacion(models.Model):
  class Meta:
    db_table = '[transversal].[tblEKOLocalizaciones]'

  id_localizacion = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        ) 
  localizacion = models.CharField(max_length = 30)
  compania = models.CharField(max_length = 5)
  fecha_actualizacion = models.DateField(auto_now=False, auto_now_add=False)
  activa = models.BooleanField()

  def __str__(self):
    return self.id_localizacion
  
class Articulo(models.Model):
  class Meta:
    db_table = '[transversal].[tblEKOArticulo]'
    
  cod_articulo = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )   
  compania = models.CharField(max_length = 5)

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

  activo = models.BooleanField

  def __str__(self):
    return self.cod_articulo

class TicketDetalle(models.Model):
  class Meta:
    db_table = '[recepcion].[tblEKOTicketDetalle]'

  id_ticket_detalle = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )  
  id_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
  cod_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
  tipo_embalaje = models.CharField(max_length = 20)
  nro_tolva = models.CharField(max_length=10)
  nro_precinto = models.IntegerField()
  peso_bruto = models.FloatField()
  # usuario_cambio_peso = models.ForeignKey(User)
  Observacion_cambio_peso = models.CharField(max_length = 100)
  fecha_cambio_peso = models.DateField(auto_now=False, auto_now_add=False)
  destare = models.FloatField()
  id_localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)
  # usuario_ingreso = models.ForeignKey(User, on_delete=models.CASCADE)
  peso_pnc = models.FloatField()
  # usuario_peso_pnc = models.ForeignKey(User, on_delete=models.CASCADE)
  fecha_peso_pnc = models.DateField(auto_now=False, auto_now_add=False)
  hora_inicial_seleccion = models.DateField(auto_now=False, auto_now_add=False)
  hora_final_seleccion = models.DateField(auto_now=False, auto_now_add=False)

  def __str__(self):
    return self.id_ticket_detalle

class TicketDetalleAdjunto(models.Model):
  class Meta:
    db_table = '[recepcion].[tblEKOTicketDetalleAdjuntos]'

  uuid = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        ) 
  id_ticket = models.ForeignKey(TicketDetalle, on_delete=models.CASCADE)
  archivo = models.CharField(max_length = 500)
  observacion = models.CharField(max_length = 1000)
  fecha = models.DateField(auto_now=False, auto_now_add=False)
  envio_correo = models.BooleanField()

  def __str__(self):
    return self.uuid

class ConfiguracionBascula(models.Model):
  class Meta:
    db_table = '[bascula].[tblEKOConfiguracionBasculas]'

  id_bascula = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        ) 
  id_acopio = models.ForeignKey(Acopio, on_delete=models.CASCADE)
  dispositivo = models.CharField(max_length = 50)
  tipo_pesaje = models.CharField(max_length=15)
  puerto = models.IntegerField()
  baudios = models.IntegerField()
  paridad = models.CharField(max_length = 1)
  bit_de_dato = models.IntegerField()
  bit_de_parada = models.IntegerField()
  cadena_car_1 = models.CharField(max_length = 15)
  cadena_car_2 = models.CharField(max_length = 15)
  cadena_car_3 = models.CharField(max_length = 15)
  tipo_indicador = models.CharField(max_length=20)
  tipo_bascula = models.CharField(max_length=20)
  ip_dispositivo = models.CharField(max_length = 50)
  observaciones = models.CharField(max_length = 150)
  peso_patron = models.FloatField()
  tolerancia = models.FloatField()
  pesaje_automatico = models.BooleanField()

  def __str__(self):
    return self.id_bascula
  
class VerificacionBascula(models.Model):
  class Meta:
    db_table = '[bascula].[tblEKOVerificacionBasculas]'

  consecutivo = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        ) 
  id_bascula = models.ForeignKey(ConfiguracionBascula, on_delete=models.CASCADE)
  usuario = models.CharField(max_length=10)
  fecha = models.DateField(auto_now=False, auto_now_add=False)
  verificacion = models.BooleanField()
  observacion = models.CharField(max_length=1000)
  dispositivo = models.CharField(max_length=50)

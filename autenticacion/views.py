from django.shortcuts import render
from django.http import HttpResponse

from django.db import connection

# Create your views here.
def home(request):
  return HttpResponse('<h1>Autenticacion</h1>')

cursor = connection.cursor()

# Santiago Ospina Idrobo 30/01/2024
# Validar login (tipo_de_accion = 3, usuario, clave)
def login(request, tipo_accion = '3', grupo = '', aplicacion = '', usuario = 'IDT', clave = '0518'):
  sql_query = f"EXEC dbGnlPlanta.dbo.spValidarLogin '{tipo_accion}', '{grupo}', '{aplicacion}', '{usuario}', '{clave}'"
  
  # Crear un cursor
  with connection.cursor() as cursor:
    cursor.execute(sql_query)

    results = cursor.fetchall()

  if len(results) is not 0:
    return HttpResponse(f"<h1>Response: {results}</h1>")
  else:
    return HttpResponse(f"<h1>Credenciales invalidas</h1>")

# Revisar permisos a la aplicacion (tipo_de_accion = 1, aplicacion, usuario)
  
# Filtrar los acopios a los que el usuario tiene acceso (usuario y aplicacion)
  
# validar permisos por grupos (tipo_de_accion = 2, idGrupo, idAplicacion)
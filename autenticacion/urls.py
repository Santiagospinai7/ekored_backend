from django.contrib import admin
from django.urls import path
from autenticacion import views as autenticacionViews

urlpatterns = [
  path('', autenticacionViews.home),
  path('login', autenticacionViews.login),
  path('validar_permiso_aplicacion', autenticacionViews.validar_permiso_aplicacion)
]
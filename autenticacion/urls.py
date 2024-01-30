from django.contrib import admin
from django.urls import path
from autenticacion import views as autenticacionViews

urlpatterns = [
  path('', autenticacionViews.home),
  path('validate', autenticacionViews.login)
]
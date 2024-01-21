from django.contrib import admin
from django.urls import path
from seleccion import views as seleccionViews

urlpatterns = [
  path('', seleccionViews.home),
]
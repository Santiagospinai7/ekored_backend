from django.contrib import admin
from django.urls import path
from recepcion import views as recepcionViews

urlpatterns = [
  path('', recepcionViews.home),
]
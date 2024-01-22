from django.contrib import admin
from .models import tblEKOProveedores, tblEKOAcopio, tblEKOTicket, tblEKOZona

# Register your models here.
admin.site.register(tblEKOProveedores)
admin.site.register(tblEKOAcopio)
admin.site.register(tblEKOTicket)
admin.site.register(tblEKOZona)

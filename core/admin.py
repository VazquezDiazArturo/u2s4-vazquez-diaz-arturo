# admin: el módulo que arma el panel /admin automáticamente
from django.contrib import admin
# Servicio: el modelo que escribiste en models.py, importado desde este mismo directorio
from .models import Servicio

# register: le dice a Django "mostrá este modelo en el panel /admin, con un CRUD ya armado"
admin.site.register(Servicio)

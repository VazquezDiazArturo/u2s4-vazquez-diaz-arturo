from django.shortcuts import render
from django.db import connection
# Servicio: el modelo definido en models.py, importado desde este mismo directorio
from .models import Servicio


def inicio(request):
    info_bd = connection.settings_dict
    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }
    return render(request, 'core/inicio.html', contexto)


def servicios(request):
    # .objects.all(): un QuerySet — Django lo traduce a un SELECT * FROM core_servicio
    # ya no es una lista fija de diccionarios como en la Semana 3
    lista_servicios = Servicio.objects.all()
    return render(request, 'core/servicios.html', {'servicios': lista_servicios})

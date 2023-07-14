from django.shortcuts import render, get_object_or_404
from .models import Proyecto

def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'rumo_app/detalle_proyecto.html', {'proyecto': proyecto})

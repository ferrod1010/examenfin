from django.shortcuts import render
from django.contrib import messages
from .forms import GradoForm
from universidad.models import Grado, Asignacion, Materia



def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'])
            for actor_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, grado_id = grado.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Grado Guardado Exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'universidad/grado_editar.html', {'formulario': formulario})

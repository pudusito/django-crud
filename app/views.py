# Create your views here.
from app.models import Empleado
from django.shortcuts import render, redirect
from django.db.models import Q
from . import forms

""" Vista para el formulario de empleados"""
def index(request):
    form =forms.EmpleadoForm()
    if request.method=='POST':
        form=forms.EmpleadoForm(request.POST)
        if form.is_valid():
            print("Formulario OK")
            print("Nombre: ",form.cleaned_data['nombre'])
            #ver información procesada desde el form
            form.save()
            return listar_empleados(request)
    data={'form':form}
    return render(request,'app/index.html',data)


def listar_empleados(request):
    empleados = Empleado.objects.all()
    print(f"Empleados: {empleados}")  # Debugging print
    data = {'empleados': empleados}
    return render(request, 'app/empleados.html', data)


def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)  # Buscar el registro a editar
    form = forms.EmpleadoForm(instance=empleado)
    if request.method == 'POST':
        form = forms.EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()  # Aquí actualiza el registro en lugar de crear uno nuevo
            return listar_empleados(request)  # redirect('employee_list')
    else:
        data = {'form': form}
        return render(request, 'app/index.html', data)
    

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('trabajadores:empleados')



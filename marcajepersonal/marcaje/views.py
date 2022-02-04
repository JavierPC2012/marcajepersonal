from contextlib import redirect_stdout
import datetime
from datetime import datetime
from socket import TIPC_IMPORTANCE
from unittest import expectedFailure
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from marcaje.models import marcajes, usuarios

# Create your views here.
def añadir_usuario(request):
    try:
        codigoEmpleado=request.POST["codigoEmpleado"]
        nombreCompleto=request.POST["nombreCompleto"]
        puesto=request.POST['puesto']
        busqueda_usuario=usuarios.objects.filter(codigo__exact=codigoEmpleado).values('codigo','nombre','puesto')
        if len(busqueda_usuario)!=0:
            messages.info(request,'Codigo de empleado duplicado. Intenta con otro')
            #return redirect('/add_nuevo_usuario/')
            return render(request, 'ingreso_nuevo_usuario.html', {'alerta':'error'})
        else:
            usuarios.objects.create(codigo=codigoEmpleado,nombre=nombreCompleto,puesto=puesto)
            messages.info(request,'Usuario Agregado!')
            return render(request, 'ingreso_nuevo_usuario.html', {'alerta':'info'})
    except:
        return render(request, 'ingreso_nuevo_usuario.html', {})

def marcaje_entrada(request):
    try:
        codigoEmpleado=request.POST["codigoEmpleado"]
        now = datetime.now()
        tipo="Entrada"
        busqueda_usuario=usuarios.objects.filter(codigo__exact=codigoEmpleado).values('codigo','nombre','puesto')
        if len(busqueda_usuario)==1:
            marcajes.objects.create(codigo=codigoEmpleado,fecha=now,tipo=tipo)
            messages.info(request,'Marcaje Entrada Exitoso!')
            return render(request, 'marcaje_entrada.html', {'alerta':'info'})
        else:
            messages.info(request,'Codigo de empleado no encontrado. Intenta con otro')
            return render(request, 'marcaje_entrada.html', {'alerta':'error'})
    except:
        return render(request, 'marcaje_entrada.html', {})

def marcaje_salida(request):
    try:
        codigoEmpleado=request.POST["codigoEmpleado"]
        now = datetime.now()
        tipo="Salida"
        busqueda_usuario=usuarios.objects.filter(codigo__exact=codigoEmpleado).values('codigo','nombre','puesto')
        if len(busqueda_usuario)==1:
            marcajes.objects.create(codigo=codigoEmpleado,fecha=now,tipo=tipo)
            messages.info(request,'Marcaje Salida Exitoso!')
            return render(request, 'marcaje_salida.html', {'alerta':'info'})
        else:
            messages.info(request,'Codigo de empleado no encontrado. Intenta con otro')
            return render(request, 'marcaje_salida.html', {'alerta':'error'})
    except:
        return render(request, 'marcaje_salida.html', {})

def control_panel(request):
    try:
        codigoEmpleado=request.POST["codigoEmpleado"]
        lista_usuarios=usuarios.objects.all().values('codigo','nombre','puesto')
        usuario=usuarios.objects.filter(codigo__exact=codigoEmpleado).values('codigo','nombre','puesto')
        lista_marcajes=marcajes.objects.filter(codigo__exact=codigoEmpleado).values('codigo','fecha','tipo')
        return render(request, 'control_panel.html', {'lista_usuarios':lista_usuarios,'usuario':usuario,'lista_marcajes':lista_marcajes})
    except:
        lista_usuarios=usuarios.objects.all().values('codigo','nombre','puesto')
        return render(request, 'control_panel.html', {'lista_usuarios':lista_usuarios})
        
        








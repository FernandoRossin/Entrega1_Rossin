from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from app_uni.models import *
from django.template import loader
from app_uni.forms import *
# Create your views here.

def inicio(request):

    return render(request, "inicio.html")


def carga_estudiante(request):
    
    if request.method == "POST":
        
        mi_formulario = Estudiante_formulario(request.POST)
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre = datos['nombre'], apellido = datos['apellido'], email = datos['email'] )
            estudiante.save()
            return render(request,"carga_estudiante.html")


    return render(request, "carga_estudiante.html")

def carga_profesor(request):
    
    if request.method == "POST":
        
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre = datos['nombre'], apellido = datos['apellido'], email = datos['email'], profesion = datos['profesion'])
            profesor.save()
            return render(request,"carga_profesor.html")

    return render(request, "carga_profesor.html")
    

def carga_curso(request):

    if request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre = datos['nombre'], camada = datos['camada'])
            curso.save()
            return render(request,"carga_curso.html")


    return render(request, "carga_curso.html")
    
def buscar_curso(request):

    return render(request,"buscar_curso.html")


def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse('Campo vacio')



def bases_datos(request):
    
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    cursos = Curso.objects.all()
    
    diccionario = {
        "estudiantes": estudiantes,
        "profesores" : profesores,        
        "cursos": cursos }

    todos_los_datos = loader.get_template("bases_datos.html")
    datos = todos_los_datos.render(diccionario)
    
    return HttpResponse(datos)
    


    
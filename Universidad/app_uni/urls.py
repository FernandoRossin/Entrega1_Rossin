from django.urls import path
from . import views

urlpatterns = [

    path("", views.inicio, name="inicio"),
    path("carga_curso", views.carga_curso, name="carga_curso"),
    path("carga_estudiante", views.carga_estudiante, name="carga_estudiante"),
    path("carga_profesor", views.carga_profesor, name="carga_profesor"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar, name="buscar"),
    path("bases_datos", views.bases_datos, name="bases_datos")
    
]





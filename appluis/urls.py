from django.urls import path
from appluis.views import *

urlpatterns = [
    path("cursos/",curso, name="Cursos"),
    path("", inicio, name="Inicio"),
    path("estudiantes/",estudiante, name="Estudiantes"),
    path("entregas/",entregable, name="Entregables"),
]

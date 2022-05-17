from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso2 = Curso(nombre = "C#", comision = "123456")
    curso2.save()

    documentoDeTexto = f"--> Curso: {curso2.nombre}     Comision: {curso2.comision}"

    return HttpResponse(documentoDeTexto)

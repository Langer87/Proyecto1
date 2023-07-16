from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
	return HttpResponse("<br><br>Ya entendimos esto, es muy simple.")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es:<br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: {nombre}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    miHtml = open("F:\CODERHOUSE\VSC\PythonProyecto1\Proyecto1\Proyecto1\plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
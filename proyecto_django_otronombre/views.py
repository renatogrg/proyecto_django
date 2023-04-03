from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context


def mi_vista(request):
    print('PASE POR ACA!!!!!')
    return HttpResponse('<h1>Mi primera vista</h1>')

def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    return HttpResponse(f'<p>{dt_formateado}</p>')

def saludar(request, nombre, apellido):
    return HttpResponse(f'<h1>Hola {nombre} {apellido}</h1>')

def mi_primer_template(request):

    archivo = open(r'C:\Users\rs200\OneDrive\Escritorio\proyectos\proyecto_django\templates\mi_primer_template.html', 'r')

    template = Template(archivo.read())

    archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)
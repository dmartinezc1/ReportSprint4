from django.http import HttpResponse
from . import utils

def reporte(request):
    resp = "Para ver el reporte de empresas ingrese a: 'reporte/Empresas/'" + "\n"
    resp = resp + "Para ver el reporte de los créditos ingrese a: 'reporte/Creditos/'"
    return HttpResponse("<pre>"+resp+"</pre>")

def reporteCreditos(request):
    return HttpResponse("<pre>"+utils.reportesCredito()+"</pre>")

def reporteEmpresas(request):
    return HttpResponse("<pre>"+utils.reportesEmpresas()+"</pre>")
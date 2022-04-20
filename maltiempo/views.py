from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np
# hemos creado un metodo index que devuelve una respuesta http
def index(request):
    return HttpResponse("Hola, Analucía")
def bye(request):
    return HttpResponse("Adios, Analucía")
def busqueda_coches(request):
    
    return render(request, "home.html")

def result(request):
    modelo = request.GET['model']
    cls = joblib.load(modelo+".sav")

    precio = [] 
    
    precio.append(request.GET['km'])
    precio.append(request.GET['year'])
    precio.append(request.GET['cubicCapacity'])
    precio.append(request.GET['door'])
    precio.append(request.GET['hp'])
    

    ans = cls.predict([precio])
  
    return render(request,"result.html",{'ans': ("%.2f"% ans).rstrip('0').rstrip(',')})
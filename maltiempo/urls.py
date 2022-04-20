
# AQUI SE DEFINEN LAS RUTAS LOCALES DE ESTA APLICACION
from django.urls import path
#Aqui estamos importando el views de cochespia
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('busqueda', views.busqueda_coches, name='busqueda'), 
    path('result/',views.result,name='result'),
    path('bye', views.bye, name='bye'),
]

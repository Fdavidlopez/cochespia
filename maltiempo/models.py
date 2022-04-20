from django.db import models
#clase que facilita a convertir objetos en un registro y viceversa
#orm -> object relational model (trasforma un objeto en un registro o viceversa)
# leng prog objetos: objetos - tablas 
class Tiempo(models.Model):
    pronostico = models.CharField(max_length=200)
    fecha  = models.DateTimeField('date published')
  

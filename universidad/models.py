from django.db import models
from django.contrib import admin


#Define la clase Actor, esta tabla no se relaciona con nadie más.

class Materia(models.Model):
    nombre  =   models.CharField(max_length=30)
    profesor  =   models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
# Create your models here.

class Grado(models.Model):
    nombre    = models.CharField(max_length=60)
    seccion      = models.CharField(max_length=60)
    materias   = models.ManyToManyField(Actor, through='Asignacion')
    def __str__(self):
        return self.nombre

class Asignacion (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)

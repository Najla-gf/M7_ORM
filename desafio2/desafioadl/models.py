from django.db import models

class Tarea(models.Model):
    descripcion = models.TextField(max_length=400, default='')
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=400, default='')
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

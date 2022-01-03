from django.db import models

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descripcion')
    portada = models.ImageField(null=True, blank=True, upload_to='portfolio')
    url = models.URLField(null=True, blank=True, verbose_name='Direccion web')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.title
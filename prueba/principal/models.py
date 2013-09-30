#encoding:utf-8
from django.db import models

# Create your models here.
class Fotos (models.Model):
	titulo=models.CharField(max_length=100, verbose_name='Título', unique=True)
	imagen = models.ImageField(upload_to='files_prueba/fotos', verbose_name='Imágen')
	fecha = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.titulo
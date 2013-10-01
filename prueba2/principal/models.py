#encoding:utf-8
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Fotos (models.Model):
	titulo=models.CharField(max_length=100, verbose_name='Título', unique=True)
	imagen = models.ImageField(upload_to='fotos', verbose_name='Imágen')
	fecha = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.titulo

@receiver(post_delete, sender=Fotos)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.imagen.storage, photo.imagen.path
    storage.delete(path)
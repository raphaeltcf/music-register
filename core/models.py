from django.db import models
from django.db.models.deletion import DO_NOTHING



class Music(models.Model):
    music = models.CharField(max_length=50, verbose_name='Nome da musica')
    author = models.CharField(max_length=50, verbose_name='Autor da musica')
    band = models.CharField(max_length=50, verbose_name='Banda')

    class Meta:
        verbose_name_plural = 'Musica'

    def __str__(self):
        return self.music



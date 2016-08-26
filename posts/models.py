from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=140)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    fechita = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fechita = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
from django.db import models

# Create your models here.


class Eventos(models.Model):
    foto = models.ImageField(null=True,blank=True)
    nome = models.CharField(max_length=150)
    data = models.DateField()
    texto = models.TextField()
    local = models.CharField(max_length=150)


class Cultos(models.Model):
    foto = models.ImageField(null=True,blank=True)
    nome = models.CharField(max_length=150)
    pastor = models.CharField(max_length=150)
    data = models.DateField()

class Novidades(models.Model):
    foto = models.ImageField(null=True,blank=True)
    nome = models.CharField(max_length=150)
    texto = models.TextField()
    
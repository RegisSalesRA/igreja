from django.db import models

# Create your models here.


class Eventos(models.Model):

    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=150)
    data = models.DateTimeField(null=False, blank=False)
    texto = models.TextField()
    local = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return self.nome


class Cultos(models.Model):

    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=150)
    pastor = models.CharField(max_length=150)
    data = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Culto'
        verbose_name_plural = 'Cultos'

    def __str__(self):
        return self.nome    
class Novidades(models.Model):

    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=150)
    texto = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Novidade'
        verbose_name_plural = 'Novidades'
    
    def __str__(self):
        return self.nome    
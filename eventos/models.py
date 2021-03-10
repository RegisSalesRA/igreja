from django.db import models


class Eventos(models.Model):

    foto = models.ImageField(upload_to='eventos',null=True, blank=True)
    nome = models.CharField(max_length=150)
    data = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=True, blank=True)
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

    foto = models.ImageField(upload_to='cultos',null=True, blank=True)
    tema = models.CharField(max_length=150)
    descricao = models.TextField()
    pastor = models.CharField(max_length=150)
    data = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Culto'
        verbose_name_plural = 'Cultos'

    def __str__(self):
        return self.tema

class Novidades(models.Model):

    foto = models.ImageField(upload_to='novidades',null=True, blank=True)
    nome = models.CharField(max_length=150)
    texto = models.TextField()
    
    contato = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Novidade'
        verbose_name_plural = 'Novidades'
    
    def __str__(self):
        return self.nome    
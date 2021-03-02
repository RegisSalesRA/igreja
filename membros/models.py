from django.db import models
from rest_framework import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from igreja.models import Igreja, Celula


class Ministerio(models.Model):
    MUSICA = 'Musica'
    ORACAO = 'Oracao'
    INTEGRACAO = 'Integracao'
    ESTUDO_BIBLICO = 'Integracao'

    ministerio_opcoes = [
        (MUSICA, 'Musica'),
        (ORACAO, 'Oracao'),
        (INTEGRACAO, 'Integracao'),
        (ESTUDO_BIBLICO, 'Integracao')
    ]

    ministerio = models.CharField(max_length=100, choices=ministerio_opcoes)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Ministerio'
        verbose_name_plural = 'Ministerios'

    def __str__(self):
        return self.ministerio

class Jovens(models.Model):

    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=150, null=False, blank=False)
    igreja = models.ForeignKey(Igreja, null=False, blank=False, on_delete=models.CASCADE)
    celula = models.ForeignKey(Celula, null=True, blank=True, on_delete=models.CASCADE)
    ministerio = models.ForeignKey(Ministerio, on_delete=models.CASCADE)
    contato = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        verbose_name = 'Jovem'
        verbose_name_plural = 'Jovens'

    def __str__(self):
        return self.nome
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from registros.models import RegistroPessoal
from igreja.models import Igreja, Celula


class Ministerio(models.Model):
    MUSICA = 'Musica'
    ORACAO = 'Oracao'
    INTEGRACAO = 'Integracao'

    ministerio_opcoes = [
        (MUSICA, 'Musica'),
        (ORACAO, 'Oracao'),
        (INTEGRACAO, 'Integracao')
    ]

    ministerio = models.CharField(max_length=100, choices=ministerio_opcoes)

    class Meta:
        verbose_name = 'Ministerio'
        verbose_name_plural = 'Ministerios'

    def __str__(self):
        return self.ministerio

class Jovens(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    igreja = models.ForeignKey(Igreja, null=False, blank=False, on_delete=models.CASCADE)
    celula = models.ForeignKey(Celula, null=True, blank=True,
                               on_delete=models.CASCADE)
    ministerio = models.ForeignKey(Ministerio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Jovem'
        verbose_name_plural = 'Jovens'

    def __str__(self):
        return self.nome


class Novatos(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    descreva = models.TextField(help_text='Descreva algo sobre voce')

    class Meta:
        verbose_name = 'Novato'
        verbose_name_plural = 'Novatos'

    def __str__(self):
        return self.nome

from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from apps.registros.models import RegistroPessoal
from apps.igreja.models import Igreja, Celula

#
# class Usuario(AbstractUser):
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     nome = models.CharField(max_length=100, null=False, blank=False)
#
#     def __str__(self):
#         return self.username
#
# # CODIGO PARA GERAR TOKEN TODA VEZ QUE CRIAR UM USUARIO
#
# @receiver(post_save, sender=Usuario)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#

class Jovens(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    funcao_na_igreja = models.TextField(help_text='Descreva algo sobre voce')
    igreja = models.ForeignKey(Igreja, null=False, blank=False, on_delete=models.CASCADE)
    celula_atual = models.ForeignKey(Celula, related_name='JovensDaCelula', null=False, blank=False,
                                     on_delete=models.CASCADE)
    RegistreSeusDados = models.ForeignKey(RegistroPessoal, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Jovem'
        verbose_name_plural = 'Jovens'

    def __str__(self):
        return self.nome

class Novatos(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    igreja_participante = models.ForeignKey(Igreja, null=False, blank=False, on_delete=models.CASCADE)
    celular_participante = models.ForeignKey(Celula, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Novato'
        verbose_name_plural = 'Novatos'

    def __str__(self):
        return self.nome
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Jovens, Novatos



# Register your models here.

@admin.register(Jovens)
class JovensAdmin(admin.ModelAdmin):
    list_display = ['nome', 'funcao_na_igreja', 'igreja', 'celula_atual', 'RegistreSeusDados']


@admin.register(Novatos)
class NovatosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'igreja_participante', 'celular_participante']
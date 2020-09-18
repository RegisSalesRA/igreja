from django.contrib import admin

# Register your models here.
from apps.igreja.models import Celula, Igreja, Lideres


@admin.register(Igreja)
class IgrejaAdmin(admin.ModelAdmin):
    list_display = ['endereco', 'nome_igreja', 'pastor_nome', 'descreva_igreja']


@admin.register(Lideres)
class LideresAdmin(admin.ModelAdmin):
    list_display = ['nome', 'id_igreja', 'igreja_pertence']


@admin.register(Celula)
class CelulaAdmin(admin.ModelAdmin):
    list_display = ['endereco', 'nome_celula', 'igreja_mae', 'lider_celula']

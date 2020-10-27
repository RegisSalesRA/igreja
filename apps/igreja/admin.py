from django.contrib import admin

# Register your models here.
from apps.igreja.models import Celula, Igreja, Lideres


@admin.register(Igreja)
class IgrejaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'pastor', 'descricao']


@admin.register(Lideres)
class LideresAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo_igreja', 'igreja']


@admin.register(Celula)
class CelulaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'igreja', 'lider']

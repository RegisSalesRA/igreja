from django.contrib import admin

# Register your models here.
from registros.models import RegistroPessoal, RegistroAtividade


@admin.register(RegistroPessoal)
class RegistroPessoalAdmin(admin.ModelAdmin):
    list_display = ['image', 'nome_completo', 'status', 'identificacao_igreja', 'cpf', 'telefone', 'email',
                    'aniversario']


@admin.register(RegistroAtividade)
class RegistroPessoalAdmin(admin.ModelAdmin):
    list_display = ['nome_atividade', 'file', 'descreva_atividade', 'Data', 'created_at', 'update_at', 'igreja_mae']

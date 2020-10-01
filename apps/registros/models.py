import uuid
from django.db import models
from stdimage import StdImageField

from apps.igreja.models import Igreja


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class RegistroPessoal(models.Model):
    statusoptions = [
        ('J', 'Jovem'),
        ('P', 'Pastor'),
        ('L', 'Lider')
    ]

    image = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}, blank=True, null=True)
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=6, default='J', choices=statusoptions)
    identificacao_igreja = models.CharField(max_length=20, null=True, blank=True, unique=True)
    cpf = models.CharField(max_length=20, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True, default=None)
    aniversario = models.DateTimeField(default=None)

    class Meta:
        verbose_name = 'Registro Pessoal'
        verbose_name_plural = 'Registros Pessoais'

    def __str__(self):
        return self.nome_completo


class RegistroAtividade(models.Model):
    nome_atividade = models.CharField(max_length=150, null=False, blank=False, unique=True)
    file = models.FileField(upload_to='Registros', null=True, blank=True)
    descreva_atividade = models.TextField()
    Data = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    igreja_mae = models.ForeignKey(Igreja, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_atividade
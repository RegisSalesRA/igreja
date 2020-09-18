import uuid
from django.db import models

# Create your models here.
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Igreja(models.Model):
    endereco = models.CharField(max_length=200, null=False, blank=False)
    nome_igreja = models.CharField(max_length=200, null=False, blank=False)
    pastor_nome = models.CharField(max_length=150, null=False, blank=False)
    descreva_igreja = models.TextField(help_text='fale um pouco sobre a igreja')

    def __str__(self):
        return self.nome_igreja


class Lideres(models.Model):
    image = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    nome = models.CharField(max_length=150, null=False, blank=False)
    id_igreja = models.CharField(max_length=150, null=False, blank=False)
    igreja_pertence = models.ForeignKey(Igreja, related_name='lideres', null=False, blank=False,
                                        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Lider'
        verbose_name_plural = 'Lideres'

    def __str__(self):
        return self.nome


class Celula(models.Model):
    endereco = models.CharField(max_length=200, null=False, blank=False)
    nome_celula = models.CharField(max_length=200, null=False, blank=False)
    igreja_mae = models.ForeignKey(Igreja, related_name='Igreja_nome_mae', null=False, blank=False,
                                   on_delete=models.CASCADE)
    lider_celula = models.ForeignKey(Lideres, related_name='JovensDaCelula', null=False, blank=False,
                                     on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Celula'
        verbose_name_plural = 'Celulas'

    def __str__(self):
        return self.nome_celula
import uuid
from django.db import models

# Create your models here.
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Igreja(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField(help_text='Sobre a igreja')
    pastor = models.CharField(max_length=150, null=False, blank=False)
    descricao_pastor = models.TextField(help_text='Um pouco da historia do pastor')
    endereco = models.CharField(max_length=200, null=False, blank=False)
    
    foto = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)                      
    
    class Meta:
        verbose_name = 'Igreja'
        verbose_name_plural = 'Igrejas'
    
    def __str__(self):
        return self.nome


class Lideres(models.Model):
    descricao = models.TextField()
    contato = models.CharField(max_length=18)
    nome = models.CharField(max_length=150, null=False, blank=False)
    codigo_igreja = models.CharField(max_length=150, null=False, blank=False)
    igreja = models.ForeignKey(Igreja, null=False, blank=False,
                               on_delete=models.CASCADE)

    foto = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        verbose_name = 'Lider'
        verbose_name_plural = 'Lideres'

    def __str__(self):
        return self.nome



class Ministerio(models.Model):
    MUSICA = 'Musica'
    ORACAO = 'Oracao'
    INTEGRACAO = 'Integracao'
    ESTUDO_BIBLICO = 'Estudo_biblico'

    ministerio_opcoes = [
        (MUSICA, 'Musica'),
        (ORACAO, 'Oracao'),
        (INTEGRACAO, 'Integracao'),
        (ESTUDO_BIBLICO, 'Estudo_biblico')
    ]

    ministerio = models.CharField(max_length=100, choices=ministerio_opcoes)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Ministerio'
        verbose_name_plural = 'Ministerios'

    def __str__(self):
        return self.ministerio


class Celula(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    endereco = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField()
    contato = models.CharField(max_length=12)
    igreja = models.ForeignKey(Igreja, null=False, blank=False,
                               on_delete=models.CASCADE)
    lider = models.ForeignKey(Lideres, null=True, blank=True,
                              on_delete=models.CASCADE)
    ministerio = models.ForeignKey(Ministerio, null=True, blank=True,
                              on_delete=models.CASCADE)
    
    foto = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        verbose_name = 'Celula'
        verbose_name_plural = 'Celulas'

    def __str__(self):
        return self.nome
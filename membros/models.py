from django.db import models
from igreja.models import Igreja, Celula, Ministerio


class Jovens(models.Model):

    foto = models.ImageField(upload_to='membros',null=True, blank=True)
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

    def __repr__(self):
        return f'Jovem: {self.nome}'

    def __str__(self):
        return f'Jovem: {self.nome}'
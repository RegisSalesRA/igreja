# ViewHtml

# RegistroAtividadedeHtml
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, CreateView
from rest_framework import viewsets

from api.registros.serializers import RegistroAtividadeSerializer, RegistroPessoalSerializer
from apps.registros.models import RegistroPessoal, RegistroAtividade


class ViewRegistroAtividade(viewsets.ModelViewSet):
    queryset = RegistroAtividade.objects.all()
    serializer_class = RegistroAtividadeSerializer


class ViewRegistroPessoal(viewsets.ModelViewSet):
    queryset = RegistroPessoal.objects.all()
    serializer_class = RegistroPessoalSerializer
    # Permissao de Autentificacao
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)




class RegistroAtividadeHtml(ListView):
    model = RegistroAtividade
    template_name = 'RegistroAtividade.html'
    queryset = RegistroAtividade.objects.all()
    context_object_name = 'RegistrosA'


class RegistroAtividadeCreateHtml(CreateView):
    model = RegistroAtividade
    template_name = 'RegistroAtividade_form.html'
    fields = ['nome_atividade', 'descreva_atividade', 'Data', 'igreja_mae']
    success_url = reverse_lazy('atividadeHtml')


class RegistroAtividadeUpdateHtml(UpdateView):
    model = RegistroAtividade
    template_name = 'RegistroAtividade_form.html'
    fields = ['nome_atividade', 'descreva_atividade', 'Data', 'igreja_mae']
    success_url = reverse_lazy('atividadeHtml')


class RegistroAtividadeDeleteHtml(DeleteView):
    model = RegistroAtividade
    template_name = 'RegistroAtividade_form_deletar.html'
    success_url = reverse_lazy('atividadeHtml')


# RegistroAtividadeEnd

# RegistroPessoal

class RegistroPessoalHtml(ListView):
    model = RegistroPessoal
    template_name = 'RegistroPessoal.html'
    queryset = RegistroPessoal.objects.all()
    context_object_name = 'RegistrosP'


class RegistroPessoalCreateHtml(CreateView):
    model = RegistroPessoal
    template_name = 'RegistroPessoal_form.html'
    fields = ['nome_completo', 'status', 'identificacao_igreja', 'cpf', 'telefone', 'email', 'aniversario']
    success_url = reverse_lazy('pessoalHtml')


class RegistroPessoalUpdateHtml(UpdateView):
    model = RegistroPessoal
    template_name = 'RegistroPessoal_form.html'
    fields = ['nome_completo', 'status', 'identificacao_igreja', 'cpf', 'telefone', 'email', 'aniversario']
    success_url = reverse_lazy('pessoalHtml')


class RegistroPessoalDeleteHtml(DeleteView):
    model = RegistroPessoal
    template_name = 'RegistroPessoal_form_deletar.html'
    success_url = reverse_lazy('pessoalHtml')

# RegistroPessoalEnd

# HtmlEnd
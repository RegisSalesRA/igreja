# RegistroAtividadedeHtml
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, CreateView
from registros.models import RegistroPessoal, RegistroAtividade

class RegistroPessoalHtml(ListView):
    model = RegistroPessoal
    template_name = 'registros/RegistroPessoal.html'
    queryset = RegistroPessoal.objects.all()
    context_object_name = 'RegistrosP'


class RegistroPessoalCreateHtml(CreateView):
    model = RegistroPessoal
    template_name = 'registros/RegistroPessoal_form.html'
    fields = ['nome_completo', 'status', 'identificacao_igreja', 'cpf', 'telefone', 'email', 'aniversario']
    success_url = reverse_lazy('pessoalHtml')


class RegistroPessoalUpdateHtml(UpdateView):
    model = RegistroPessoal
    template_name = 'registros/RegistroPessoal_form.html'
    fields = ['nome_completo', 'status', 'identificacao_igreja', 'cpf', 'telefone', 'email', 'aniversario']
    success_url = reverse_lazy('pessoalHtml')


class RegistroPessoalDeleteHtml(DeleteView):
    model = RegistroPessoal
    template_name = 'registros/RegistroPessoal_form_deletar.html'
    success_url = reverse_lazy('pessoalHtml')
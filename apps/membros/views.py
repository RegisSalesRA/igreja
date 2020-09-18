from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.membros.models import Jovens, Novatos

# ViewHtml

class JovensViewHtml(ListView):
    model = Jovens
    template_name = 'jovem.html'
    queryset = Jovens.objects.all()
    context_object_name = 'Jovens'


class JovensCreateHtml(CreateView):
    model = Jovens
    template_name = 'jovem_form.html'
    fields = ['nome', 'funcao_na_igreja', 'igreja', 'celula_atual', 'RegistreSeusDados']
    success_url = reverse_lazy('jovemHtml')


class JovensUpdateHtml(UpdateView):
    model = Jovens
    template_name = 'jovem_form.html'
    fields = ['nome', 'funcao_na_igreja', 'igreja', 'celula_atual', 'RegistreSeusDados']
    success_url = reverse_lazy('jovemHtml')

class JovensDeleteHtml(DeleteView):
    model = Jovens
    template_name = 'jovem_form_deletar.html'
    success_url = reverse_lazy('jovemHtml')

# ViewHtmlEndJovem

# ViewHtmlNovato

class NovatoViewHtml(ListView):
    model = Novatos
    template_name = 'novato.html'
    queryset = Novatos.objects.all()
    context_object_name = 'Novatos'

class NovatoCreateHtml(CreateView):
    model = Novatos
    template_name = 'novato_form.html'
    fields = ['nome','igreja_participante','celular_participante']
    success_url = reverse_lazy('novatoHtml')

class NovatoUpdateHtml(UpdateView):
    model = Novatos
    template_name = 'novato_form.html'
    fields = ['nome', 'igreja_participante', 'celular_participante']
    success_url = reverse_lazy('novatoHtml')

class NovatoDeleteHtml(DeleteView):
    model = Novatos
    template_name = 'novato_form_deletar.html'
    success_url = reverse_lazy('novatoHtml')
# ViewHtmlEndNovato

# ViewHtmlEnd
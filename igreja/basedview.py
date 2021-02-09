class IgrejaView(ListView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja.html'
    queryset = Igreja.objects.all()
    context_object_name = 'igreja'


class CreateIgrejaView(CreateView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja_form.html'
    fields = ['nome', 'endereco', 'pastor', 'descricao']
    success_url = reverse_lazy('igrejaHtml')


class UpdateIgrejaView(UpdateView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja_form.html'
    fields = ['nome', 'endereco', 'pastor', 'descricao']
    success_url = reverse_lazy('igrejaHtml')


class DeleteIgrejaView(DeleteView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja_form_deletar.html'
    success_url = reverse_lazy('igrejaHtml')


# IgrejaEnd Crud


# Lider Crud


class LiderView(ListView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider.html'
    queryset = Lideres.objects.all()
    context_object_name = 'lideres'


class CreateLiderView(CreateView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider_form.html'
    fields = ['nome', 'codigo_igreja', 'igreja']
    success_url = reverse_lazy('liderHtml')


class UpdateLiderView(UpdateView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider_form.html'
    fields = ['nome', 'codigo_igreja', 'igreja']
    success_url = reverse_lazy('liderHtml')


class DeleteLiderView(DeleteView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider_form_deletar.html'
    success_url = reverse_lazy('liderHtml')


# LiderEnd Crud


# Celula Crud

class CelulaView(ListView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula.html'
    queryset = Celula.objects.all()
    context_object_name = 'celula'


# List Celulas
class ListaCelulaView(ListView):
    model = Celula
    template_name = 'igreja/celulas.html'
    queryset = Celula.objects.all()
    context_object_name = 'celulalista'


class CreateCelulaView(CreateView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula_form.html'
    fields = ['nome_celula', 'endereco', 'igreja_mae', 'lider_celula']
    success_url = reverse_lazy('celulaHtml')


class UpdateCelulaView(UpdateView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula_form.html'
    fields = ['nome_celula', 'endereco', 'igreja_mae', 'lider_celula']
    success_url = reverse_lazy('celulaHtml')


class DeleteCelulaView(DeleteView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula_form_deletar.html'
    success_url = reverse_lazy('celulaHtml')


# EndCelula Crud
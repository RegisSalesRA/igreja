from django.urls import path
from rest_framework.routers import SimpleRouter
from apps.membros.views import jovens, jovensForm, jovenUpdate, jovemDelete, novatos, novatoDelete, novatosForm, \
    novatoUpdate,mocidade

# membrosUrl = SimpleRouter()
# membrosUrl.register('jovem', JovensView)
# membrosUrl.register('novato', NovatosView)

urlpatterns = [

    # Api
    # path('jovens/', JovensView, name='jovens'),
    # path('novatos/', NovatosView, name='novatos'),
    # ApiEnd

    # HtmlUrl
    path('igrejas/', mocidade, name='mocidade'),

    path('jovens/', jovens, name='jovens'),
    path('jovemcreate/', jovensForm, name='jovemcreate'),
    path('jovemAtualizar/<int:jovem_id>', jovenUpdate, name='jovemAtualizar'),
    path('jovemDeletar/<int:jovem_id>', jovemDelete, name='jovemDeletar'),

    path('novatos/', novatos, name='novatos'),
    path('novatocreate/', novatosForm, name='novatocreate'),
    path('novatoAtualizar/<int:novato_id>', novatoUpdate, name='novatoAtualizar'),
    path('novatoDeletar/<int:novato_id>', novatoDelete, name='novatoDeletar'),

    # HtmlUrlEnd
]
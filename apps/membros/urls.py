from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.membros.views import JovensView, NovatosView, jovens, jovensForm, jovenUpdate, jovemDelete,novatos,novatoDelete,novatosForm,novatoUpdate

membrosUrl = SimpleRouter()

membrosUrl.register('jovem', JovensView)
membrosUrl.register('novato', NovatosView)

urlpatterns = [

    # Api
    # path('jovens/', JovensView, name='jovens'),
    # path('novatos/', NovatosView, name='novatos'),
    # ApiEnd

    # HtmlUrl

    path('Jovens/', jovens, name='Jovens'),
    path('jovemcreate/', jovensForm, name='jovemcreate'),
    path('JovemAtualizar/<int:jovem_id>', jovenUpdate, name='JovemAtualizar'),
    path('jovemDeletar/<int:jovem_id>', jovemDelete, name='jovemDeletar'),

    path('Novatos/', novatos, name='Novatos'),
    path('novatocreate/', novatosForm, name='novatocreate'),
    path('novatoAtualizar/<int:novato_id>', novatoUpdate, name='novatoAtualizar'),
    path('novatoDeletar/<int:novato_id>', novatoDelete, name='novatoDeletar'),

    # HtmlUrlEnd
]
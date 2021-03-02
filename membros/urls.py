from django.urls import path
from rest_framework.routers import SimpleRouter
from membros.views import jovens, jovensForm, jovenUpdate, jovemDelete, mocidade, mocidadelista
from membros.filter import filtrocategoria, categoriafiltro,jovem_search


urlpatterns = [

    path('mocidade/', mocidade, name='mocidade'),
    path('mocidade/<int:igreja_id>', mocidadelista, name='mocidadelista'),
    path('categoria_search/', filtrocategoria, name='filtrocategoria'),
    path('jovem_search/', jovem_search, name='jovem_search'),
    path('categoria/<int:categoria_id>', categoriafiltro, name='categoriafiltro'),
    

    path('jovens/', jovens, name='jovens'),
    path('jovemcreate/', jovensForm, name='jovemcreate'),
    path('jovemAtualizar/<int:jovem_id>', jovenUpdate, name='jovemAtualizar'),
    path('jovemDeletar/<int:jovem_id>', jovemDelete, name='jovemDeletar'),
]
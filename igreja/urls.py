from django.urls import path
from igreja.views.filter import (igreja_search,celula_musica,celula_estudo,celula_integracao,
                           celula_oracao,celula_ministerio_detail,celula_ministerio_musica_detail,
                           celula_ministerio_oracao_detail,celula_ministerio_integracao_detail,
                           celula_ministerio_estudo_detail,
                           )
from igreja.views.views import (home, igreja, igrejas, celula, celulas,lideres,
                          lider,deletar_celula,FormCelula, deleteigreja,
                          jovens_celula,
                           )

urlpatterns = [
    # Home
    path('', home, name='home'),

    # List View
    path('igrejas/', igrejas, name='igrejas'),
    path('igreja/<int:igreja_id>/', igreja, name='igreja'),
    path('igrejas/', igreja_search, name='igreja_search'),
    path('igreja/<int:igreja_id>/celulas/', celulas, name='celulas'),
    path('igreja/<int:igreja_id>/celula/<int:celula_id>/', celula, name='celula'),
    path('igreja/<int:igreja_id>/celula/<int:celula_id>/jovens/', jovens_celula, name='jovens_celula'),
    path('igreja/<int:igreja_id>/lideres/', lideres , name='lideres'),
    path('igreja/<int:igreja_id>/lider/<int:lider_id>/', lider, name='lider'),

    # List View Ministerios
    path('igreja/<int:igreja_id>/celulas/ministerio/<int:celula_id>/', celula_ministerio_detail, name='celula_ministerio_detail'),
    path('igreja/<int:igreja_id>/celulas/ministerio_musica/<int:celula_id>/detalhes', celula_ministerio_musica_detail, name='celula_ministerio_musica_detail'),
    path('igreja/<int:igreja_id>/celulas/ministerio_integracao/<int:celula_id>/detalhes', celula_ministerio_integracao_detail, name='celula_ministerio_integracao_detail'),
    path('igreja/<int:igreja_id>/celulas/ministerio_oracao/<int:celula_id>/detalhes', celula_ministerio_oracao_detail, name='celula_ministerio_oracao_detail'),
    path('igreja/<int:igreja_id>/celulas/ministerio_estudo/<int:celula_id>/detalhes', celula_ministerio_estudo_detail, name='celula_ministerio_estudo_detail'),
    
    #filtro
    path('igreja/<int:igreja_id>/celulas/ministerio_musica/', celula_musica, name='celula_musica'),
    path('igreja/<int:igreja_id>/celulas/ministerio_oracao/', celula_oracao, name='celula_oracao'),
    path('igreja/<int:igreja_id>/celulas/ministerio_integracao/', celula_integracao, name='celula_integracao'),
    path('igreja/<int:igreja_id>/celulas/ministerio_estudo/', celula_estudo, name='celula_estudo'),

    # Deletar
    path('igreja/deletar/<int:igreja_id>', deleteigreja, name='deleteigreja'),
    path('celula/deletar/', deletar_celula, name='deletar_celula'),
    path('celula/form/<int:celula_id>/', FormCelula, name='formcelula'),
    # HTML END
]
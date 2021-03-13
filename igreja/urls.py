from django.urls import path
from igreja.views.filter import (igreja_search,celula_musica,celula_estudo,celula_integracao,
                           celula_oracao,celula_ministerio_detail,celula_ministerio_musica_detail,
                           celula_ministerio_oracao_detail,celula_ministerio_integracao_detail,
                           celula_ministerio_estudo_detail,
                           )
from igreja.views.views import (home, igreja, igrejas, celula, celulas,lideres,
                          lider,deletar_celula,FormCelula, deleteigreja,
                          jovens_celula,dashboard_index,
                           )

from igreja.views.crud import (dashboard_igrejas,dashboard_igrejas_create,
dashboard_igrejas_update,dashboard_igrejas_delete,dashboard_celulas,
dashboard_celulas_create,dashboard_celulas_delete,dashboard_celulas_update,
dashboard_lideres_create,dashboard_lideres_delete,dashboard_lideres_update,dashboard_lideres,
dashboard_ministerios,dashboard_ministerios_update,dashboard_ministerios_delete,dashboard_ministerios_create)


urlpatterns = [
    # Home
    path('', home, name='home'),
    
    # Dashboard
    path('dashboard/', dashboard_index, name='dashboard_index'),
    # Igreja
    path('dashboard_igrejas/', dashboard_igrejas, name='dashboard_igrejas'),
    path('dashboard_igrejas_create/', dashboard_igrejas_create, name='dashboard_igrejas_create'),
    path('dashboard_igrejas_update/<int:igreja_id>/', dashboard_igrejas_update, name='dashboard_igrejas_update'),
    path('dashboard_igrejas_delete/<int:igreja_id>/', dashboard_igrejas_delete, name='dashboard_igrejas_delete'),
    # Celula
    path('dashboard_celulas/', dashboard_celulas, name='dashboard_celulas'),
    path('dashboard_celulas_create/', dashboard_celulas_create, name='dashboard_celulas_create'),
    path('dashboard_celulas_update/<int:celula_id>/', dashboard_celulas_update, name='dashboard_celulas_update'),
    path('dashboard_celulas_delete/<int:celula_id>/', dashboard_celulas_delete, name='dashboard_celulas_delete'),
    # Lideres
    path('dashboard_lideres/', dashboard_lideres, name='dashboard_lideres'),
    path('dashboard_lideres_create/', dashboard_lideres_create, name='dashboard_lideres_create'),
    path('dashboard_lideres_update/<int:lider_id>/', dashboard_lideres_update, name='dashboard_lideres_update'),
    path('dashboard_lideres_delete/<int:lider_id>/', dashboard_lideres_delete, name='dashboard_lideres_delete'),
    # Ministerio
    path('dashboard_ministerios/', dashboard_ministerios, name='dashboard_ministerios'),
    path('dashboard_ministerios_create/', dashboard_ministerios_create, name='dashboard_ministerios_create'),
    path('dashboard_ministerios_update/<int:ministerio_id>/', dashboard_ministerios_update, name='dashboard_ministerios_update'),
    path('dashboard_ministerios_delete/<int:ministerio_id>/', dashboard_ministerios_delete, name='dashboard_ministerios_delete'),
    
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
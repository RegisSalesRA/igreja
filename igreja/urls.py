from django.urls import path
from igreja.filter import igreja_search,celula_musica,celula_estudo,celula_integracao,celula_oracao
from igreja.views import (home, igreja, igrejas, celula, celulas,lideres,lider,deletar_celula, 
    FormCelula, deleteigreja, signup_view, signin_view, signout_view)

urlpatterns = [
    # Home
    path('', home, name='home'),

    #Login
    path('account/criar/', signup_view, name='signup'),
    path('account/logar/', signin_view, name='signin'),
    path('account/deslogar/', signout_view, name='signout'),
    # HTML

    # List View
    path('igrejas/', igrejas, name='igrejas'),
    path('igreja/<int:igreja_id>/', igreja, name='igreja'),
    path('igreja/<int:igreja_id>/celulas/', celulas, name='celulas'),
    path('igreja/<int:igreja_id>/celula/<int:celula_id>/', celula, name='celula'),
    path('igreja/<int:igreja_id>/lideres/', lideres , name='lideres'),
    path('igreja/<int:igreja_id>/lider/<int:lider_id>/', lider, name='lider'),

    #filtro
    path('igreja/<int:igreja_id>/celulas/ministerio_musica/', celula_musica, name='celula_musica'),
    path('igreja/<int:igreja_id>/celulas/ministerio_oracao/', celula_oracao, name='celula_oracao'),
    path('igreja/<int:igreja_id>/celulas/ministerio_integracao/', celula_integracao, name='celula_integracao'),
    path('igreja/<int:igreja_id>/celulas/ministerio_estudo/', celula_estudo, name='celula_estudo'),

    #path('celulas/', celulas, name='celulas'),
    path('search/', igreja_search, name='igreja_search'),
    # Deletar
    path('igreja/deletar/<int:igreja_id>', deleteigreja, name='deleteigreja'),
    path('celula/deletar/', deletar_celula, name='deletar_celula'),
    # Deletar
    path('celula/form/<int:celula_id>/', FormCelula, name='formcelula'),
    # HTML END
]
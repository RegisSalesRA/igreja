from django.urls import path
from igreja.filter import IgrejaFiltro
from igreja.views import (home, igreja, igrejas, celula, celulas, 
    FormCelula, deleteigreja, signup_view, signin_view, signout_view,lideres)

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
    path('igreja/<int:igreja_id>/celulas', celulas, name='celulas'),

    #path('celulas/', celulas, name='celulas'),
    path('lideres/<int:igreja_id>/lideres/', lideres , name='lideres'),
    path('search/', IgrejaFiltro, name='IgrejaFiltro'),
    path('igrejas/<int:igreja_id>/celula/<int:celula_id>', celula, name='celula'),

    # Deletar
    path('igreja/deletar/<int:igreja_id>', deleteigreja, name='deleteigreja'),
    # Deletar
    path('celula/form/<int:celula_id>/', FormCelula, name='formcelula'),
    # HTML END
]

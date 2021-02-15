from django.urls import path
from rest_framework.routers import SimpleRouter
from igreja.filter import IgrejaFiltro
from igreja.views import (Home, lideres, igreja, igrejas, celula, celulas, 
    FormCelula, deleteigreja, signupView, signinView, signoutView)

urlpatterns = [
    # Home
    path('', Home, name='Home'),

    #Login
    path('account/create/', signupView, name='signup'),
    path('account/signin/', signinView, name='signin'),
    path('account/signout/', signoutView, name='signout'),
    # HTML

    # View
    path('igrejas/', igrejas, name='igrejas'),
    path('celulas/', celulas, name='celulas'),
    path('lideres/', lideres, name='lideres'),
    path('search/', IgrejaFiltro, name='IgrejaFiltro'),
    path('igrejas/<int:igreja_id>/celula/<int:celula_id>', celula, name='celula'),
    path('igrejas/<int:igreja_id>/', igreja, name='igreja'),
    
    # Deletar
    path('igreja/deletar/<int:igreja_id>', deleteigreja, name='deleteigreja'),
    # Deletar
    path('celula/form/<int:celula_id>/', FormCelula, name='formcelula'),
    # HTML END
]

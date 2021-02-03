from django.urls import path
from rest_framework.routers import SimpleRouter
from apps.igreja.filter import IgrejaFiltro
from apps.igreja.views import (IgrejaView, CreateIgrejaView, UpdateIgrejaView, DeleteIgrejaView, CelulaView,
    CreateCelulaView, UpdateCelulaView, DeleteCelulaView, LiderView, CreateLiderView, UpdateLiderView, DeleteLiderView,
    Home, ListaCelulaView, LiderLista, igreja, Igrejas, celula, Celulas, 
    FormCelula, IgrejaAjaxDeletar, deleteigreja, signupView, signinView, signoutView)

urlpatterns = [

    # path('igreja/', ViewIgreja, name='igrejas'),
    # path('igreja/<int:pk>/', ViewIgreja, name='igreja'),

    # path('lideres/', ViewLideres, name='lideres'),
    # path('lideres/<int:lideres_pk>/', ViewCelula, name='lider'),

    # path('celula/', ViewCelula, name='celulas'),

    # #Login
    # path('account/create/', signupView, name='signup'),
    # path('account/signin/', signinView, name='signin'),
    # path('account/signout/', signoutView, name='signout'),
    # # HTML

    # # No BasedView
    # path('igrejas/', Igrejas, name='igrejas'),
    # path('igrejas/<int:igreja_id>/', igreja, name='igreja'),
    # path('igrejas/<int:igreja_id>/celulas/', Celulas, name='celulas'),
    # path('igrejas/<int:igreja_id>/celula/<int:celula_id>', celula, name='celula'),
    # path('igrejas/<int:igreja_id>/lider/', LiderLista, name='lideres'),
    # path('search/', IgrejaFiltro, name='IgrejaFiltro'),
    # # Deletar
    # path('igreja/deletarajax/', IgrejaAjaxDeletar, name='ajaxdeletar'),
    # path('igreja/deletar/<int:igreja_id>', deleteigreja, name='deleteigreja'),
    # # Deletar
    # path('celula/form/<int:celula_id>/', FormCelula, name='formcelula'),
    # # No BasedView

    # path('igrejaHtml/', IgrejaView.as_view(), name='igrejaHtml'),
    # path('igrejaAdicionar/', CreateIgrejaView.as_view(), name='igrejaAdicionar'),
    # path('<int:pk>/igrejaAtualizar/', UpdateIgrejaView.as_view(), name='igrejaAtualizar'),
    # path('<int:pk>/igrejaDeletar/', DeleteIgrejaView.as_view(), name='igrejaDeletar'),

    # path('liderHtml/', LiderView.as_view(), name='liderHtml'),
    # path('liderAdicionar/', CreateLiderView.as_view(), name='liderAdicionar'),
    # path('<int:pk>/liderAtualizar/', UpdateLiderView.as_view(), name='liderAtualizar'),
    # path('<int:pk>/liderDeletar/', DeleteLiderView.as_view(), name='liderDeletar'),

    # path('celulaHtml/', CelulaView.as_view(), name='celulaHtml'),
    # path('celulaAdicionar/', CreateCelulaView.as_view(), name='celulaAdicionar'),
    # path('<int:pk>/celulaAtualizar/', UpdateCelulaView.as_view(), name='celulaAtualizar'),
    # path('<int:pk>/celulaDeletar/', DeleteCelulaView.as_view(), name='celulaDeletar'),

    # HTML END

    # Home
    path('', Home, name='Home'),
]

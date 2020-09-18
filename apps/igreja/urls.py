from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.igreja.views import IgrejaView, CreateIgrejaView, UpdateIgrejaView, DeleteIgrejaView, CelulaView, \
    CreateCelulaView, UpdateCelulaView, DeleteCelulaView, LiderView, CreateLiderView, UpdateLiderView, DeleteLiderView, \
    ViewIgreja, ViewCelula, ViewLideres


igrejaUrl = SimpleRouter()
igrejaUrl.register('igreja', ViewIgreja)
igrejaUrl.register('celula', ViewCelula)
igrejaUrl.register('lideres', ViewLideres)

urlpatterns = [

    # API
    path('igreja/', ViewIgreja, name='igrejas'),
    path('igreja/<int:pk>/', ViewIgreja, name='igreja'),

    path('lideres/', ViewLideres, name='lideres'),
    path('lideres/<int:lideres_pk>/', ViewCelula, name='lider'),

    path('celula/', ViewCelula, name='celulas'),

    # APIEND

    # HTML

    path('igreja/', IgrejaView.as_view(), name='igrejaHtml'),
    path('igrejaAdicionar/', CreateIgrejaView.as_view(), name='igrejaAdicionar'),
    path('<int:pk>/igrejaAtualizar/', UpdateIgrejaView.as_view(), name='igrejaAtualizar'),
    path('<int:pk>/igrejaDeletar/', DeleteIgrejaView.as_view(), name='igrejaDeletar'),

    path('liderHtml/', LiderView.as_view(), name='liderHtml'),
    path('liderAdicionar/', CreateLiderView.as_view(), name='liderAdicionar'),
    path('<int:pk>/liderAtualizar/', UpdateLiderView.as_view(), name='liderAtualizar'),
    path('<int:pk>/liderDeletar/', DeleteLiderView.as_view(), name='liderDeletar'),

    path('celulaHtml/', CelulaView.as_view(), name='celulaHtml'),
    path('celulaAdicionar/', CreateCelulaView.as_view(), name='celulaAdicionar'),
    path('<int:pk>/celulaAtualizar/', UpdateCelulaView.as_view(), name='celulaAtualizar'),
    path('<int:pk>/celulaDeletar/', DeleteCelulaView.as_view(), name='celulaDeletar'),

    # HTML END
]
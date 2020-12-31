from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.registros.views import (RegistroAtividadeHtml,
                                  RegistroAtividadeCreateHtml,
                                  RegistroAtividadeUpdateHtml,
                                  RegistroAtividadeDeleteHtml,
                                  RegistroPessoalHtml,
                                  RegistroPessoalCreateHtml,
                                  RegistroPessoalUpdateHtml,
                                  RegistroPessoalDeleteHtml,)


urlpatterns = [

    # Html

    path('atividadeHtml/', RegistroAtividadeHtml.as_view(), name='atividadeHtml'),
    path('atividadeAdicionar/', RegistroAtividadeCreateHtml.as_view(), name='atividadeAdicionar'),
    path('<int:pk>/atividadeAtualizar/', RegistroAtividadeUpdateHtml.as_view(), name='atividadeAtualizar'),
    path('<int:pk>/atividadeDeletar/', RegistroAtividadeDeleteHtml.as_view(), name='atividadeDeletar'),

    path('pessoalHtml/', RegistroPessoalHtml.as_view(), name='pessoalHtml'),
    path('PessoalAdicionar/', RegistroPessoalCreateHtml.as_view(), name='pessoalAdicionar'),
    path('<int:pk>/pessoalAtualizar/', RegistroPessoalUpdateHtml.as_view(), name='pessoalAtualizar'),
    path('<int:pk>/pessoalDeletar/', RegistroPessoalDeleteHtml.as_view(), name='pessoalDeletar'),

    # HtmlEnd
]

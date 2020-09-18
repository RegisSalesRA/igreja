from django.urls import path

from apps.membros.views import JovensViewHtml, JovensCreateHtml, JovensUpdateHtml, JovensDeleteHtml, NovatoViewHtml, \
    NovatoCreateHtml, NovatoUpdateHtml, NovatoDeleteHtml

urlpatterns = [
#HtmlUrl

    path('jovemHtml/', JovensViewHtml.as_view(), name='jovemHtml'),
    path('jovemAdicionar/', JovensCreateHtml.as_view(), name='jovemAdicionar'),
    path('<int:pk>/jovemAtualizar/', JovensUpdateHtml.as_view(), name='jovemAtualizar'),
    path('<int:pk>/jovemDeletar/', JovensDeleteHtml.as_view(), name='jovemDeletar'),

    path('novatoHtml/', NovatoViewHtml.as_view(), name='novatoHtml'),
    path('novatoAdicionar/', NovatoCreateHtml.as_view(), name='novatoAdicionar'),
    path('<int:pk>/novatoAtualizar/', NovatoUpdateHtml.as_view(), name='novatoAtualizar'),
    path('<int:pk>/novatoDeletar/', NovatoDeleteHtml.as_view(), name='novatoDeletar'),

#HtmlUrlEnd

]
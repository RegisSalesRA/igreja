from django.urls import path
from eventos.views.views import eventos, evento, cultos, culto, novidades, novidade 

urlpatterns = [
    path('eventos', eventos, name='eventos'),
    path('evento/<int:evento_id>/', evento, name='evento'),
    path('cultos', cultos, name='cultos'),
    path('culto/<int:culto_id>/', culto, name='culto'),
    path('novidades', novidades, name='novidades'),
    path('novidade/<int:novidade_id>/', novidade, name='novidade'),
    ]
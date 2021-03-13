from django.urls import path
from eventos.views.views import eventos, evento, cultos, culto, novidades, novidade 
from eventos.views.crud import (dashboard_eventos,dashboard_eventos_create,dashboard_eventos_delete,dashboard_eventos_update,
dashboard_cultos,dashboard_cultos_create,dashboard_cultos_delete,dashboard_cultos_update,
dashboard_novidades,dashboard_novidades_create,dashboard_novidades_delete,dashboard_novidades_update)
urlpatterns = [

    path('eventos', eventos, name='eventos'),
    path('evento/<int:evento_id>/', evento, name='evento'),
    path('cultos', cultos, name='cultos'),
    path('culto/<int:culto_id>/', culto, name='culto'),
    path('novidades', novidades, name='novidades'),
    path('novidade/<int:novidade_id>/', novidade, name='novidade'),
    # Dashboard
    path('dashboard_eventos/', dashboard_eventos, name='dashboard_eventos'),
    path('dashboard_eventos_create/', dashboard_eventos_create, name='dashboard_eventos_create'),
    path('dashboard_eventos_create/<int:evento_id>/', dashboard_eventos_update, name='dashboard_eventos_update'),
    path('dashboard_eventos_delete/<int:evento_id>/', dashboard_eventos_delete, name='dashboard_eventos_delete'), 
   
    path('dashboard_cultos/', dashboard_cultos, name='dashboard_cultos'),
    path('dashboard_cultos_create/', dashboard_cultos_create, name='dashboard_cultos_create'),
    path('dashboard_cultos_create/<int:culto_id>/', dashboard_cultos_update, name='dashboard_cultos_update'),
    path('dashboard_cultos_delete/<int:culto_id>/', dashboard_cultos_delete, name='dashboard_cultos_delete'), 
   
    path('dashboard_novidades/', dashboard_novidades, name='dashboard_novidades'),
    path('dashboard_novidades_create/', dashboard_novidades_create, name='dashboard_novidades_create'),
    path('dashboard_novidades_create/<int:novidade_id>/', dashboard_novidades_update, name='dashboard_novidades_update'),
    path('dashboard_novidades_delete/<int:novidade_id>/', dashboard_novidades_delete, name='dashboard_novidades_delete'), 
    ]
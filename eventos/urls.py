from django.urls import path
from eventos.views import eventos, cultos

urlpatterns = [
    path('eventos', eventos, name='eventos'),
    path('cultos', cultos, name='cultos'),
]
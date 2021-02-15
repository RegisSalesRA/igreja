from django.urls import path
from eventos.views import eventos

urlpatterns = [
    path('eventos', eventos, name='eventos'),
]
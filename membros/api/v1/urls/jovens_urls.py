from django.urls import path
from membros.api.v1.views import JovensListView,DetailJovensView


urlpatterns = [
    path('jovens/',JovensListView.as_view()),
    path('jovens/<int:pk>/',DetailJovensView.as_view()),
]
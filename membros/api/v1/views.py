from typing import Generic
from django.db.models.fields import GenericIPAddressField
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework import generics
from membros.api.v1.serializers import JovensSerializer
from membros.models import Jovens


class JovensListView(generics.ListCreateAPIView):
    queryset = Jovens.objects.all()
    serializer_class = JovensSerializer

class DetailJovensView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jovens.objects.all()
    serializer_class = JovensSerializer
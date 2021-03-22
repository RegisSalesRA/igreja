from membros.models import Jovens
from rest_framework import serializers


class JovensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jovens
        fields = ['id','nome','igreja','celula','ministerio','contato']
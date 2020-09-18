from rest_framework import serializers
from apps.registros.models import RegistroAtividade, RegistroPessoal


class RegistroPessoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPessoal
        fields = '__all__'


class RegistroAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAtividade
        fields = '__all__'

from rest_framework import serializers
from apps.membros.models import Jovens, Novatos

#
# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = '__all__'


class JovensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jovens
        fields = '__all__'


class NovatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novatos
        fields = '__all__'
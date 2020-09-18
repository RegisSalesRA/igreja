from rest_framework import serializers
from apps.igreja.models import Celula, Igreja, Lideres


class IgrejaSerializer(serializers.ModelSerializer):
    Igreja_nome_mae = serializers.StringRelatedField(many=True, read_only=True)
    lideres = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Igreja
        fields = ('id', 'endereco', 'nome_igreja', 'pastor_nome', 'lideres', 'Igreja_nome_mae')


class CelulaSerializer(serializers.ModelSerializer):
    JovensDaCelula = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Celula
        fields = ('__all__')


class LideresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lideres
        fields = ('__all__')

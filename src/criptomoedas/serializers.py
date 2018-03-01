from rest_framework import serializers

from .models import Moeda


class MoedaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = ('uuid', 'created_at', 'updated_at', 'nome', 'codigo')
        read_only_fields = ('uuid', 'created_at', 'updated_at')

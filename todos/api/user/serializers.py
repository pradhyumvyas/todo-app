from rest_framework import serializers

from .models import Test

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('full_name',)
from rest_framework import serializers
from .models import TestSquare
class TestSquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSquare
        fields = ('Number','SquareNumber')
'''
class TestSquareNumSalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSquare
        fields = ('Number',)'''

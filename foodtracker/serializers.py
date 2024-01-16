from rest_framework import serializers
from .models import Food, Image, User, EnergyConsumption

class FoodSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = ('__all__')


class ImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Image
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = (['username'])

class EnergyConsumptionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EnergyConsumption
        fields = ('__all__')



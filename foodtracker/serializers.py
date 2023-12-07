from rest_framework import serializers
from .models import Food, Image

class FoodSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = ('__all__')


class ImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Image
        fields = ('__all__')

from rest_framework import serializers
from .models import *


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('is_publish','internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField("is_publish")

    def is_publish(self, category):
        publish_food = Food.objects.filter(is_publish=True, category=category)
        serializer = FoodSerializer(instance=publish_food, many=True)
        return serializer.data

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')

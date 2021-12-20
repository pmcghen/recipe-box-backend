from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'slug', 'ingredients', 'activeTime', 'inactiveTime', 'directions', 'notes', 'isFeatured', 'rating')

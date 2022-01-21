from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recipe

class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Recipe.objects.all())
    avatar = serializers.ImageField(source='userprofile.avatar')
    bio = serializers.CharField(source='userprofile.bio')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bio', 'avatar', 'recipes')

class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    # The source argument used here controls which attribute is used to populate a field and can
    # point to any attribute on the serialized instance. Also note that we're using ReadOnlyField
    # which is always read-only; it can not be used for updating model instances when they are
    # serialized. We could have also used CharField(read_only=True) here to accomplish the same thing.

    class Meta:
        model = Recipe
        fields = '__all__'

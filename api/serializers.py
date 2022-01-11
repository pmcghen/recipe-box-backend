from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recipe, UserProfile
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

# https://testdriven.io/blog/drf-serializers/
class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='userprofile.avatar')
    bio = serializers.CharField(source='userprofile.bio')
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'bio', 'avatar')

class RecipeSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = UserSerializer()
    class Meta:
        model = Recipe
        fields = '__all__' # ('id', 'author', 'name', 'slug', 'ingredients', 'activeTime', 'inactiveTime', 'directions', 'notes', 'image', 'isFeatured', 'rating', 'isPrivate', 'tags')

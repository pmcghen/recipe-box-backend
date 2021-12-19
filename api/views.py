from rest_framework import viewsets

from .serializers import RecipeSerializer
from .models import Recipe

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('name')
    serializer_class = RecipeSerializer

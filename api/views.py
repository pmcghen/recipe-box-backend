from django.db.models import Q
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RecipeSerializer
from .models import Recipe

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('name')
    serializer_class = RecipeSerializer

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        recipes = Recipe.objects.filter(
            Q(name__icontains=query) | Q(ingredients__icontains=query) | Q(directions__icontains=query) | Q(notes__icontains=query))
        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data)
    else:
        return Response({"recipes": []})

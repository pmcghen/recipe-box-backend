from django.urls import include, path
from rest_framework import routers, urlpatterns
from . import views

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)

# Wire up API using automatic routing
# Include URLs for browsable API

urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.search),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

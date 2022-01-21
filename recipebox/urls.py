from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]

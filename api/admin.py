from django.contrib import admin
from .models import Recipe
from .models import User

admin.site.register(Recipe)
admin.site.register(User)

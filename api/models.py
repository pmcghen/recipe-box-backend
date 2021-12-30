from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    ingredients = models.TextField(max_length=2000)
    activeTime = models.IntegerField(blank=True, null=True)
    inactiveTime = models.IntegerField(blank=True, null=True)
    directions = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='recipes/images/', blank=True)
    notes = models.TextField(max_length=2000, blank=True, null=True)
    isFeatured = models.BooleanField(default=False)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

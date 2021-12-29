from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    ingredients = models.TextField(max_length=2000)
    activeTime = models.IntegerField(blank=True, null=True)
    inactiveTime = models.IntegerField(blank=True, null=True)
    directions = models.TextField(max_length=2000)
    notes = models.TextField(max_length=2000, blank=True, null=True)
    isFeatured = models.BooleanField(default=False)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

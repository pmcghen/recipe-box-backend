from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default='')
    avatar = models.ImageField(upload_to='avatars/', blank=True)

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveUserProfile(sender, instance, **kwargs):
    instance.userprofile.save()

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
    isPrivate = models.BooleanField(default=False)

    def __str__(self):
        return self.name

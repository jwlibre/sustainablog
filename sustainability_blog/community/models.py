from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted user')[0]

# Don't need to create users model (table), as users created by default already
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now) #could also use auto_now_add=True
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user)) #use on_delete=models.CASCADE to delete user's posts when user is deleted
    intro_paragraph = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()

    # return the title
    def __str__(self):
        return self.title

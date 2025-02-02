from django.db.models.signals import post_save #fires after a post is saved
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist

# the User, on being created, sends the signal post_save to the receiver,
# which is the create_profile function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #want this to run every time a user is created
    if created:
        Profile.objects.create(user=instance) # instance = instance of the User that was created


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #want this to run every time a user is created
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance) # required for admin login-- implies admin requires a profile, is there a fix for this?

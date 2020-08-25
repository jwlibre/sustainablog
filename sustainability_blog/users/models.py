from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# don't forget to register models within the app's admin.py file!
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self): # this is how to overwrite builtin methods
        super().save() # runs the save method of the parent class

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

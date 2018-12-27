from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AuthorProfile(models.Model):
    author_image = models.ImageField(upload_to='mainsite/static/images/')
    author = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='author_profile_image')
    def __str__(self):
        return self.author.get_full_name()

from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthorProfile(AbstractUser):
    author_image = models.ImageField(upload_to='mainsite/static/images/', null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

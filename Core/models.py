from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


# Create your models here.

class User(AbstractUser):

    avatar = models.FileField(upload_to="avatars", blank=True, null=True)
    
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
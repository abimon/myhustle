from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    contact = models.CharField(max_length=15, blank=True,null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

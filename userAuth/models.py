from django.db import models
import django.utils.timezone
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=200)
    avatar = models.ImageField(max_length=200,null=True,upload_to='images/profile')
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    updated_at = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name

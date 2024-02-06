from django.db import models
from django.conf import settings

class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,default='Public')
    community = models.CharField(max_length=100,null=True)
    file = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

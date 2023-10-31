from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(upload_to='img/')
    comment = models.CharField(max_length=100)
    user = models.CharField(max_length=30)

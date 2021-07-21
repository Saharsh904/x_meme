from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    url = models.URLField(max_length=1000000)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
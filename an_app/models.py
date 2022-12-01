from django.db import models

# Create your models here.
class PostModel(models.Model):

    name = models.CharField(max_length=100)
    content = models.TextField()


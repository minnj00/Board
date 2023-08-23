from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.Charfield()
    content = models.TextField()
    created_at = models.DateTimeField()
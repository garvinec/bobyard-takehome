from django.db import models

# Create your models here.


class Comment(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    author = models.CharField(max_length=64)
    parent = models.CharField(max_length=64, default="")
    text = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    image = models.URLField(default="", blank=True)

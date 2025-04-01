from django.db import models

# Create your models here.


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=64)
    text = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    image = models.URLField(default="", blank=True)

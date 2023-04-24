from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    author = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)








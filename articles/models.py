from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField
    author = models.CharField(max_length=100)



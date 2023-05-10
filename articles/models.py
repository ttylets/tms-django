from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    likes = models.IntegerField(default=0)


class Author (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField('date_of_birth')
    articles = models.ManyToManyField(Article, related_name='titles')






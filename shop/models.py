from django.db import models


class Product (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Category(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)

from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    summary = models.TextField(default="")
# Create your models here.

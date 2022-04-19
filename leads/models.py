from django.db import models

# Create your models here.
class Lead(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    phone_num = models.CharField(max_length=14)
    email = models.CharField(max_length=45)
    birthday = models.DateField(verbose_name="Birthday", null=True)

from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField('회사명', max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class User(models.Model):
    pass
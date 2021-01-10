from django.db import models

# Create your models here.


class Seller(models.Model):
    pass


class Product(models.Model):
    pass


class Buyer(models.Model):
    pass


class Order(models.Model):
    pass


class Country(models.Model):
    country_name = models.CharField(max_length=16,unique=True)
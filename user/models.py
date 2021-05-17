from django.db import models


class Guides(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotels(models.Model):
    
    big_city_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    meals = models.TextField(max_length=300)
    review = models.TextField(max_length=300)
    
    def __str__(self):
        return self.big_city_name 

class Tourists(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name




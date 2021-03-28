from django.db import models


class Guides(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotels(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    meals = models.CharField(max_length=100)
    review = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name 

# class Transport(models.Model):
#     name = models.CharField(max_length=100)
#     condintion = models.CharField(max_lenth=100)
#     ticket = models.CharField(max_length=100)


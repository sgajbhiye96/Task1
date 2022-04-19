from django.db import models
from django.contrib.auth.models import User





# Creating models for user Registration.

class User(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)


# Creating models for balnace in user balance

class balance(models.Model):
       user = models.ForeignKey(User,on_delete=models.CASCADE)
       balance = models.IntegerField(default = 0)


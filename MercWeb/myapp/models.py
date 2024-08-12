from django.db import models

# Create your models here.
class userProfile(models.Model):
    user = models.CharField(max_length=100),
    address = models.CharField(max_length=100),
    city = models.CharField(max_length=100),
    zipcode = models.CharField(max_length=100),

def __str__(self):
    return self.user.username
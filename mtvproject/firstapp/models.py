from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

class Reservetion(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    guess_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)


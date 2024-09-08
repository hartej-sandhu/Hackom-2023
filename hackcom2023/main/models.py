from django.db import models

# Create your models here.
class UserData(models.Model):
    homeLoaction = models.CharField(max_length=100)
    workLocation = models.CharField(max_length=100)
    workTime = models.CharField(max_length=100)
    workDays = models.CharField(max_length=100)

class outstation(models.Model):
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    seats = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    car = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

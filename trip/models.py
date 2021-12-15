from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class trip(models.Model):
    startLongitude = models.FloatField()
    startLatitude = models.FloatField()
    endLongitude = models.FloatField()
    endLatitude = models.FloatField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    date = models.DateTimeField()
    distanceTravelled = models.FloatField()
    userId=models.ForeignKey(User,on_delete=models.CASCADE)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=100)
    transportationMethod = models.CharField(max_length=100)
    jobPosition = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
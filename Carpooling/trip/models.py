from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class trip(models.Model):
    startLongitude = models.FloatField()
    startLatitude = models.FloatField()
    endLongitude = models.FloatField()
    endLatitude = models.FloatField()
    startTime = models.DateTimeField()
    userId = models.ForeignKey(User,on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=100)
    transportationMethod = models.CharField(max_length=100)
    jobPosition = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
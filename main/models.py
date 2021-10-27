from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Campaign(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True)
    websiteURL = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)
    campaignName = models.CharField(max_length=255, blank=True)
    campaignTagline = models.TextField(blank=True)
    category = models.CharField(max_length=255, blank=True)
    startdate = models.DateTimeField(default=timezone.now)
    enddate = models.DateTimeField(default=timezone.now)
    pitchCampaignName = models.CharField(max_length=255, blank=True)
    pitchFile = models.FileField(upload_to="files/", null=True, blank=True)
    vidlink = models.CharField(max_length=255, blank=True)
    campaignPitch = models.CharField(max_length=255, blank=True)
    campaignGoal = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=255, blank=True)
    rewardfile = models.FileField(upload_to="files/", null=True, blank=True)
    shippingInfo = models.TextField(blank=True)
    rewarddetails = models.TextField(blank=True)
    deliveryTime = models.DateTimeField(default=timezone.now)
    faqs = models.TextField(blank=True)
    is_complete = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname

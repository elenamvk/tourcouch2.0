from __future__ import unicode_literals

from django.db import models

# Create your models here.

class House(models.Model):
    owners      = models.ManyToManyField(houserowners.Houseowner)
    name        = models.CharField(max_length=200)
    location    = models.CharField(max_length=500)
    photo       = models.URLField(max_length=255)
    description = models.CharField(max_length=500)

    wifi        = models.BooleanField(default=False)
    parking     = models.BooleanField(default=False)
    n_beds      = models.CharField(max_length=200)
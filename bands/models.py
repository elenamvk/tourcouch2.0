from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Band(models.Model):
    components  = models.ManyToManyField(artists.Artist)
    name        = models.CharField(max_length=200)
    location    = models.CharField(max_length=500)
    photo       = models.URLField(max_length=255)
    description = models.CharField(max_length=500)
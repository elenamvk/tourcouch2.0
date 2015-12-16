from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Request(models.Model):
    by_band     = models.ForeignKey(bands.Band, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    location    = models.CharField(max_length=500)
    when        = models.DateField()
    text        = models.CharField(max_length=500)
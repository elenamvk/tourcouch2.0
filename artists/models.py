from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Arist(models.Model):
    role        = models.ForeignKey(people.Person, on_delete=models.CASCADE)
    name        = models.CharField(max_length=200)
    location    = models.CharField(max_length=500)
    photo       = models.URLField(max_length=255)
    description = models.CharField(max_length=500)
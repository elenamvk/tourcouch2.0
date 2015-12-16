from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Person(models.Model):
    # name        = models.CharField(max_length=200)
    # photo       = models.URLField(max_length=255)
    # description = models.CharField(max_length=500)
    # # photo       = models.ImageField(upload_to="pictures", max_length=200, blank=False, null=False, help_text='800w x 500h')

class Person(models.Model):
    ARTIST = 'A'
    HOUSEOWNER = 'H'
    ROLES = (
        (ARTIST, 'Artist'),
        (HOUSEOWNER, 'Houseowner'),
    )
    role = models.CharField(max_length=1,
                                      choices=ROLES,
                                      default=ARTIST)

    # def is_upperclass(self):
    #     return self.year_in_school in (self.JUNIOR, self.SENIOR)
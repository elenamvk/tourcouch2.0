from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Answer(models.Model):
    to_request_n  = models.ForeignKey(requests.Request, on_delete=models.CASCADE)
    by_houseowner = models.ForeignKey(houseowners.Houseowner, on_delete=models.CASCADE)
    text          = models.CharField(max_length=500)
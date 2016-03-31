from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class Musician(models.Model):
    artist_name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return self.artist_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

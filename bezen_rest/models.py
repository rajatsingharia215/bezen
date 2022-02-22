from re import M
from django.db import models

from datetime import datetime
import uuid

# Create your models here.


class Fish(models.Model):
    fish_id = models.AutoField(primary_key=True)
    fish_name = models.CharField(max_length=50,default='')
    fish_species = models.CharField(max_length=50,default='')
    img = models.ImageField(upload_to="images/",blank = True )
    weight = models.FloatField(default=2.0)
    length = models.FloatField(default=0.5)
    lattitude = models.FloatField(default=28.70)
    longitude = models.FloatField(default=77.10)
    timestamp = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# class FishImage(models.Model):
#     img_id = models.AutoField(primary_key=True)
#     fish_id = models.ForeignKey(Fish)


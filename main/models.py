from django.db import models
from django.utils import timezone

class exercise(models.Model):
    name = models.CharField(max_length=30)
    equip = models.CharField(max_length=50)
    muscles = models.CharField(max_length=50)
    risk = models.CharField(max_length=50)
    motion = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    level = models.IntegerField()
    time = models.IntegerField()
    space = models.IntegerField()
    

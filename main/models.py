from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class exercise(models.Model):
    name = models.CharField(max_length=30)
    equip = models.CharField(max_length=15)
    muscles = models.CharField(max_length=15)
    risk = models.CharField(max_length=15)
    motion = models.CharField(max_length=10)
    level = models.IntegerField()
    time = models.IntegerField()
    space = models.IntegerField()
    details = models.TextField()

    def __str__(self):
        return self.name
    

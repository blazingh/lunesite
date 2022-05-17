from django.db import models
from django.utils import timezone

class exer(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

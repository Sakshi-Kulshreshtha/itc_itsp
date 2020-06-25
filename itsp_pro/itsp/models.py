from django.db import models
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length=20)
    t_id=models.CharField(max_length=20)
    members = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
        
# Create your models here.

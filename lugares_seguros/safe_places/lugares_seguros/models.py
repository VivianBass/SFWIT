from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

class Place(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    
    def __str__(self):
        return self.name


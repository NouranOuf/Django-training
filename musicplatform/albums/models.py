
from django.db import models
from django.utils import timezone
from artists.models import Artist

# Create your models here.
class Album (models.Model):
    # 1 to m relation an artist has many albums
    
    artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length = 60 ,default='New Album')
    creation_date = models.DateField(default=timezone.now)
    release_date = models.DateField(default=timezone.now)
    cost = models.FloatField(blank=False)
    is_approved= models.BooleanField(default=False)
          
    def __str__(self):
        return self.name


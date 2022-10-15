
from django.db import models


# Create your models here.
class Artist(models.Model):
    default_mail_value = 'blank',
    stage_name = models.CharField( max_length=60 , unique=True , blank=False)
    social_link = models.CharField( max_length=100 , default=default_mail_value , null=False)
    approved_albums=models.IntegerField(default=0)
    
    def __str__(self):
        return self.stage_name


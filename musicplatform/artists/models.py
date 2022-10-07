from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Artist(models.Model):
    default_mail_value = 'blank',
    stage_name = models.CharField( max_length=60 , unique=True , blank=False)
    social_link = models.CharField( max_length=100 , default=default_mail_value , null=False)
    def __str__(self):
        return self.stage_name
from django.contrib import admin

from albums.models import Album

# Register your models here.
from .models import Artist 

admin.site.register(Artist)
admin.site.register(Album)

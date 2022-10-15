
from django.contrib import admin
from albums.models import Album
from .models import Artist 

class AlbumInline(admin.TabularInline):
     model = Album
     readonly_fields = ["creation_date"]
     
class ArtistAdmin(admin.ModelAdmin):
     list_display = ['stage_name','approved_albums']
     inlines = [
         AlbumInline,
     ]
   
     

admin.site.register(Artist , ArtistAdmin) 
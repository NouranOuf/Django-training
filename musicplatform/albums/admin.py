
from django.contrib import admin
from .models import Album

# Register your models here.
@admin.register(Album)
class AlbumDataAdmin(admin.ModelAdmin):
  readonly_fields = ["creation_date"] 
  fieldsets = (
     (None, {
            'fields': ('is_approved','name','artist_id' ,'release_date','cost' , 'creation_date'),
            'description': "Approve the album if its name is not explicit"
        }),
    )
 
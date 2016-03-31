from django.contrib import admin

#s Register your models here.
from .models import Album, Musician


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1


class MusicianAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['artist_name']}),
    ]
    inlines = [AlbumInline]

admin.site.register(Musician, MusicianAdmin)

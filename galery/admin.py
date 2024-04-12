from django.contrib import admin
from galery.models import Photo

class ListPhotos(admin.ModelAdmin):
    list_display: list = ["id", "name", "subtitle"]
    list_display_links: list = ["id", "name"]
    search_fields: list = ["name"]

admin.site.register(Photo, ListPhotos)


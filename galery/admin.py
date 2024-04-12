from django.contrib import admin
from galery.models import Photo

class ListPhotos(admin.ModelAdmin):
    list_display: list = ["id", "name", "subtitle"]
    list_display_links: list = ["id", "name"]
    search_fields: list = ["name"]
    list_filter: list = ["category"]
    list_per_page = 10

admin.site.register(Photo, ListPhotos)


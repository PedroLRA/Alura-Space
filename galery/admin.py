from django.contrib import admin
from galery.models import Photo

class ListPhotos(admin.ModelAdmin):
    list_display: list = ["id", "name", "subtitle", "publish"]
    list_display_links: list = ["id", "name"]
    search_fields: list = ["name"]
    list_filter: list = ["category", "user"]
    list_editable: list = ["publish"]
    list_per_page: int = 10

admin.site.register(Photo, ListPhotos)


from django.shortcuts import render, get_object_or_404
from galery.models import Photo

def index(request):
    photos = Photo.objects.filter(publish=True).order_by("-date")

    # Filtering by search html query
    getRequest = request.GET
    if getRequest and getRequest['search']:
        photos = photos.filter(name__icontains=getRequest['search'])

    return render(request, 'galery/index.html', {"photos": photos})

def image(request, photoId):
    photo = get_object_or_404(Photo, pk=photoId)
    return render(request, 'galery/image.html', {"photo": photo})
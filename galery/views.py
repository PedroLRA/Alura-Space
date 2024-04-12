from django.shortcuts import render, get_object_or_404
from galery.models import Photo

def index(request):
    photos = Photo.objects.filter(publish=True).order_by("-date")
    return render(request, 'galery/index.html', {"photos": photos})

def image(request, photoId):
    photo = get_object_or_404(Photo, pk=photoId)
    return render(request, 'galery/image.html', {"photo": photo})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.galery.models import Photo
from apps.galery.forms import PhotoForms

@login_required
def index(request):
    photos = Photo.objects.filter(publish=True).order_by("-date")

    # Filtering by search html query
    getRequest = request.GET
    if getRequest and getRequest['search']:
        photos = photos.filter(name__icontains=getRequest['search'])

    return render(request, 'galery/index.html', {"photos": photos})

@login_required
def filter(request, category):
    photos = Photo.objects.filter(publish=True, category=category).order_by("-date")
    
    return render(request, 'galery/index.html', {"photos": photos})

@login_required
def image(request, photoId):
    photo = get_object_or_404(Photo, pk=photoId)
    return render(request, 'galery/image.html', {"photo": photo})

@login_required
def new_image(request):
    if request.method == 'POST':
        form = PhotoForms(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada com sucesso')
            return redirect('index')

    form = PhotoForms()      
    return render(request, 'galery/new_image.html', {'form': form})

@login_required
def edit_image(request, photoId):
    photo = get_object_or_404(Photo, id=photoId)

    if not request.user == photo.user:
        messages.error(request, 'Ação não permitida')
        return redirect('index')

    if request.method == 'POST':
        form = PhotoForms(request.POST, request.FILES, instance=photo, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso')
            return redirect('index')

    form = PhotoForms(instance=photo, edit=True)
    return render(request, 'galery/edit_image.html', {'form': form, 'photoId': photoId})

@login_required
def delete_image(request, photoId):
    photo = get_object_or_404(Photo, id=photoId)

    if not request.user == photo.user:
        messages.error(request, 'Ação não permitida')
        return redirect('index')
    
    photo.delete()
    messages.success(request, 'Fotografia deletada com sucesso')
    return redirect('index')
    
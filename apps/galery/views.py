from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galery.models import Photo
from apps.galery.forms import PhotoForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não conectado')
        return redirect('login')
    
    photos = Photo.objects.filter(publish=True).order_by("-date")

    # Filtering by search html query
    getRequest = request.GET
    if getRequest and getRequest['search']:
        photos = photos.filter(name__icontains=getRequest['search'])

    return render(request, 'galery/index.html', {"photos": photos})

def image(request, photoId):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não conectado')
        return redirect('login')
        
    photo = get_object_or_404(Photo, pk=photoId)
    return render(request, 'galery/image.html', {"photo": photo})

def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não conectado')
        return redirect('login')

    if request.method == 'POST':
        form = PhotoForms(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada com sucesso')
            return redirect('index')

    form = PhotoForms()      
    return render(request, 'galery/new_image.html', {'form': form})

def edit_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não conectado')
        return redirect('login')
    
    raise NotImplementedError

def delete_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não conectado')
        return redirect('login')
    
    raise NotImplementedError
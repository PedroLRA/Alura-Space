from django.shortcuts import render

def index(request):
    return render(request, 'galery/index.html')

def image(request):
    return render(request, 'galery/image.html')
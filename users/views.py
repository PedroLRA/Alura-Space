from django.shortcuts import render
from users.forms import LoginForms, RegisterForms

def login(request):
    form = LoginForms()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForms()
    return render(request, 'users/register.html', {'form': form})

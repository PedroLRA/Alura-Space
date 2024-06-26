from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from apps.users.forms import LoginForms, RegisterForms

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if not form.is_valid(): # form info is invalid
            messages.error(request, 'Erro ao fazer login')
            return redirect('login')

        username = form['username'].value()
        password = form['password'].value()

        user = auth.authenticate(request, username=username, password=password)
        
        if user is None: # User not authenticated
            messages.error(request, 'Informações não conferem')
            return redirect('login')
        
        auth.login(request, user=user)
        messages.success(request, f'Usuário {username} logado com sucesso!')
        return redirect('index')

    form = LoginForms()
    if request.GET.get('next'): # Check if the user was redirected to login page
        messages.error(request, 'Usuário precisa estar conectado')    
    return render(request, 'users/login.html', {'form': form})

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST)
    
        if not form.is_valid(): # form info is invalid
            return render(request, 'users/register.html', {'form': form})

        username = form['username'].value()
        email = form['email'].value()
        password = form['password'].value()
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        
        messages.success(request, f'Usuário {username} criado com sucesso!')
        return redirect('login')
    
    form = RegisterForms()
    return render(request, 'users/register.html', {'form': form})

@require_http_methods(['GET'])
def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário desconectado com sucesso!')
    return redirect('login')
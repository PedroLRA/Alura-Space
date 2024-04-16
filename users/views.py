from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from users.forms import LoginForms, RegisterForms

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if not form.is_valid(): # form info is invalid
            return redirect('login')

        username = form['username'].value()
        password = form['password'].value()

        user = auth.authenticate(request, username=username, password=password)
        
        if user is None: # User not authenticated
            return redirect('login')
        
        auth.login(request, user=user)
        return redirect('index')

    form = LoginForms()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST)
    
        if not form.is_valid(): # form info is invalid
            return redirect('register')

        username = form['username'].value()
        email = form['email'].value()
        password = form['password'].value()
        passwordConfirm = form['passwordConfirm'].value()
        
        if password != passwordConfirm: # password confirmation check
            return redirect('register')

        #if user already exists
        if User.objects.filter(username=username).exists(): 
            return redirect('register')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        
        return redirect('login')
    
    form = RegisterForms()
    return render(request, 'users/register.html', {'form': form})

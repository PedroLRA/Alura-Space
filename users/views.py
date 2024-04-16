from django.shortcuts import render
from users.forms import LoginForms, RegisterForms

def login(request):
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

from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    username = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite seu nome'
            }
        )
    )
    password = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 50,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class RegisterForms(forms.Form):
    username = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite seu nome'
            }
        )
    )
    
    email = forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'SeuEmail@email.com'
            }
        )
    )

    password = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 50,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    passwordConfirm = forms.CharField(
        label = 'Confirme sua senha',
        required = True,
        max_length = 50,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Confirme sua senha'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username:
            username = username.strip()
            if ' ' in username:
                raise forms.ValidationError('"Username" não deve conter espaços.')
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Usuário já existente')
            else:
                return username
            
    def clean_passwordConfirm(self):
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')

        if password and passwordConfirm:
            if password != passwordConfirm: # password confirmation check
                raise forms.ValidationError('As senhas não conferem')
            else:
                return passwordConfirm
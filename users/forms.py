from django import forms

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
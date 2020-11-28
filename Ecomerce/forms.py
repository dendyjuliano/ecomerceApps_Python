from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'typed username',
                'class':'form-control'
            }
        )
    )

    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'typed password',
                'class':'form-control'
            }
        )
    )
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

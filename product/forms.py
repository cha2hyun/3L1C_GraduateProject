from django import forms
from django.contrib.auth.models import User
from .models import *


class uploadCom(forms.ModelForm):
    class Meta:
        model = DataDb
        fields = ['title', 'photo', 'location', 'price', 'howtotrade']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

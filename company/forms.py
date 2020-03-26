from django import forms
from django.contrib.auth.models import User
from .models import *


class createCom(forms.ModelForm):
    class Meta:
        model = CompanyDb
        fields = ['Project_Name', 'Brand_Name',
                  'Address', 'Phone_Number', 'Email', ]


class uploadCom(forms.ModelForm):
    class Meta:
        model = DataDb
        fields = ['text', 'date']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

from django import forms
from django.contrib.auth.models import User
from .models import *


class createSite(forms.ModelForm):
    class Meta:
        model = createDb
        fields = ['Project_Name', 'Category', 'board_count']

from django.urls import path
from .views import *
app_name = 'dashboard'

urlpatterns = [
    path('create/', create, name='create'),
    path('', dashboard, name='dashboard'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]

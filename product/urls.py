from django.urls import path
from .views import *
app_name = 'product'

urlpatterns = [
    #path('', create, name='create'),
    path('<str:Project_Name>/', view, name='view'),
    path('<str:Project_Name>/upload', upload, name='upload'),
    path('<str:Project_Name>/detail/<int:pk>', detail, name='detail'),
    path('<str:Project_Name>/update/<int:pk>',
         update, name='update'),
    path('<str:Project_Name>/delete/<int:pk>', delete, name='delete'),
    path('<str:Project_Name>/login/', signin, name='login'),
    path('<str:Project_Name>/register/', register, name='register'),
    path('<str:Project_Name>/logout/', signout, name='logout'),
]

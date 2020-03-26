from django.urls import path
#from django.contrib.auth import views as auth_view
from .views import signin, register, signout

app_name = 'account'
urlpatterns = [
    path('', signin, name='signin'),
    path('logout/', signout, name='logout'),
    path('register/', register, name='register')

]

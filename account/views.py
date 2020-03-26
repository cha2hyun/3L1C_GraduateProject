from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
# Create your views here.


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return redirect('/')
        else:
            return redirect('/register')
    else:
        user_form = RegisterForm()

        return render(request, 'account/register.html', {'form': user_form})


def signout(request):

    logout(request)

    return redirect('/')

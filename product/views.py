from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from .forms import *
from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout


def view(request, Project_Name):
    theme_view = DataDb.objects.filter(Project_Name=Project_Name)
    return render(request, 'product/view.html', {'theme_view': theme_view, 'Project_Name': Project_Name})


def upload(request, Project_Name):

    if request.method == "POST":
        form = uploadCom(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.Project_Name = Project_Name
            form.save()
            return redirect(reverse('product:view', args=[Project_Name]))
    else:
        form = uploadCom()
    return render(request, 'product/upload.html', {'form': form})


class BoardUpdateView(UpdateView):
    model = DataDb
    fields = ['title', 'photo', 'location', 'price', 'howtotrade']
    template_name = 'product/update.html'

    def get_success_url(self):
        return resolve_url('product:view', self.kwargs.get('Project_Name'))


def update(request, Project_Name, pk):
    update_saved = DataDb.objects.get(pk=pk)
    if request.method == "POST":
        form = uploadCom(request.POST, request.FILES)
        if form.is_valid():
            update_saved.title = form.cleaned_data['title']
            update_saved.photo = form.cleaned_data['photo']
            update_saved.location = form.cleaned_data['location']
            update_saved.price = form.cleaned_data['price']
            update_saved.howtotrade = form.cleaned_data['howtotrade']
            update_saved.save()
            return redirect(reverse('product:view', args=[Project_Name]))
    else:

        form = uploadCom(instance=update_saved)

    return render(request, 'product/update.html', {'form': form, 'Project_Name': Project_Name})


def detail(request, Project_Name, pk):
    detail_a = DataDb.objects.filter(pk=pk)

    return render(request, 'product/detail.html', {'detail_a': detail_a, 'Project_Name': Project_Name})


def delete(request, Project_Name, pk):
    delete_a = DataDb.objects.filter(pk=pk)
    delete_a.delete()
    return redirect(reverse('product:view', args=[Project_Name]))


def signin(request, Project_Name):
    logout(request)

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('product:view', args=[Project_Name]))
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'product/login.html', {'form': form, 'Project_Name': Project_Name})


def register(request, Project_Name):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return redirect(reverse('product:login', args=[Project_Name]))
        else:
            return redirect(reverse('product:register', args=[Project_Name]))
    else:
        user_form = RegisterForm()

        return render(request, 'product/register.html', {'form': user_form, 'Project_Name': Project_Name})


def signout(request, Project_Name):

    logout(request)

    return redirect(reverse('product:view', args=[Project_Name]))

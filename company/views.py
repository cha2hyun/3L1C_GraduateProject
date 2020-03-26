from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from company.forms import *
from company.models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout


def create(request):
    form = createCom(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('/dashboard',)
    return render(request, 'company/create.html', {'form': form})


def view(request, Project_Name):
    theme_view = DataDb.objects.filter(Project_Name=Project_Name)
    return render(request, 'company/view.html', {'theme_view': theme_view, 'Project_Name': Project_Name})


def upload(request, Project_Name):
    form = uploadCom(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.Project_Name = Project_Name
        form.save()
        return redirect(reverse('company:view', args=[Project_Name]))
    return render(request, 'company/upload.html', {'form': form})


def update(request, Project_Name, pk):
    update_saved = DataDb.objects.get(pk=pk)
    if request.method == "POST":
        form = uploadCom(request.POST)
        if form.is_valid():
            update_saved.text = form.cleaned_data['text']
            update_saved.date = form.cleaned_data['date']
            update_saved.save()
            return redirect(reverse('company:view', args=[Project_Name]))
    else:

        form = uploadCom(instance=update_saved)

    return render(request, 'company/update.html', {'form': form, 'Project_Name': Project_Name})


def detail(request, Project_Name, pk):
    detail_a = DataDb.objects.filter(pk=pk)

    return render(request, 'company/detail.html', {'detail_a': detail_a, 'Project_Name': Project_Name})


def delete(request, Project_Name, pk):
    delete_a = DataDb.objects.filter(pk=pk)
    delete_a.delete()
    return redirect(reverse('company:view', args=[Project_Name]))


def signin(request, Project_Name):
    logout(request)

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('company:view', args=[Project_Name]))
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'company/login.html', {'form': form, 'Project_Name': Project_Name})


def register(request, Project_Name):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return redirect(reverse('company:login', args=[Project_Name]))
        else:
            return redirect(reverse('company:register', args=[Project_Name]))
    else:
        user_form = RegisterForm()

        return render(request, 'company/register.html', {'form': user_form, 'Project_Name': Project_Name})


def signout(request, Project_Name):

    logout(request)

    return redirect(reverse('company:view', args=[Project_Name]))

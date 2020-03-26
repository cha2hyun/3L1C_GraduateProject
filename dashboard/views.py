from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *


def create(request):
    form = createSite(request.POST or None)
    form2 = request.POST.get('save', '')

    if form.is_valid():
        if form2 == 'save':
            form = form.save(commit=False)
            form.Saved = '1'
          #  form.user = request.user
          #  asd = CompanyDb.objects.filter(user=form.user)
          #  b = True
          #  for i in asd:
          #      if form.Project_Name == str(i):
          #          b = False
          #  if b == True:
            form.save()
        else:
            form = form.save(commit=False)
         #   form.user = request.user
         #   asd = CompanyDb.objects.filter(user=form.user)
         #   b = True
         #   for i in asd:
         #       if form.Project_Name == str(i):
         #           b = False
         #   if b == True:
            form.save()
        return redirect('/',)
    return render(request, 'dashboard/create.html', {'form': form})


def dashboard(request):
    th4 = createDb.objects.all()
    return render(request, 'dashboard/dashboard.html', {'th4': th4})


def update(request, pk):
    update_saved = createDb.objects.get(pk=pk)
    if request.method == "POST":
        form = createSite(request.POST)
        form2 = request.POST.get('save', '')
        if form.is_valid():
            if form2 == 'save':
                update_saved.Project_Name = form.cleaned_data['Project_Name']
                update_saved.Category = form.cleaned_data['Category']
                update_saved.board_count = form.cleaned_data['board_count']
                update_saved.Saved = '1'
                update_saved.save()
            else:
                update_saved.Project_Name = form.cleaned_data['Project_Name']
                update_saved.Category = form.cleaned_data['Category']
                update_saved.board_count = form.cleaned_data['board_count']
                update_saved.Saved = '0'
                update_saved.save()

            return redirect('/')
    else:

        form = createSite(instance=update_saved)

    return render(request, 'dashboard/update.html', {'form': form})


def delete(request, pk):
    delete_a = createDb.objects.filter(pk=pk)
    delete_a.delete()
    return redirect('/')

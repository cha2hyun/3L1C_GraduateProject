from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from company.models import CompanyDb


def dashboard(request):
    if request.user.is_authenticated:
        th4 = CompanyDb.objects.all()
        return render(request, 'dashboard/dashboard.html', {'th4': th4})
    else:
        return redirect('/')

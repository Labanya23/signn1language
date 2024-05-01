from django.shortcuts import redirect, render


def home(request):
    return render(request, 'Main/home.html')


def base(request):
    return render(request, 'base.html')

from django.shortcuts import redirect, render


def base(request):
    return render(request, 'base.html')

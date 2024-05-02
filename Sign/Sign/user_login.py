from django.shortcuts import redirect, render


def register(request):
    return render(request, 'registration/register.html')

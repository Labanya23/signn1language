"""
URL configuration for Sign project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views, user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('single/course', views.single_course, name='single_course'),
    path('contact', views.contact_us, name='contact_us'),
    path('about', views.about_us, name='about_us'),

    path('accounts/register/', user_login.register, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('do_login', user_login.do_login, name='do_login'),
    path('accounts/profile/', user_login.profile, name='profile'),
    path('accounts/profile/update',user_login.profile_update,name='profile_update'),
]

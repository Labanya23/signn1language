from django.shortcuts import redirect, render


def home(request):
    return render(request, 'Main/home.html')


def base(request):
    return render(request, 'base.html')


def single_course(request):
    return render(request, 'Main/single_course.html')


def contact_us(request):
    return render(request, 'Main/contact_us.html')

def Profile_Update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')



def about_us(request):
    return render(request, 'Main/about_us.html')

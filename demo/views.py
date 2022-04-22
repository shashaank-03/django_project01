from django.shortcuts import redirect, render
from .models import adduser


def studata(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
       
        new_user = adduser(username=username, email=email, password=password, phone = phone)
        new_user.save()

    return render(request, 'hello.html', {})

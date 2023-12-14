from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# from .models import placce
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credintials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pswd = request.POST['password']
        cpswd = request.POST['password1']
        if pswd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "the username already taken. Choose another one")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "the email address is already taken.choose another one")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                                password=pswd)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password missmatches")
            print("password is not match")
            return render(request, 'register.html')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['conpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print('username taken')
                return redirect(' register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                print('email taken')
                return redirect('register')
            else:

                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                )
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, 'Password Not Match')
            print('password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
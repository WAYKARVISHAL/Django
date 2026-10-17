from django.shortcuts import render, redirect
from .models import User


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            return render(
                request,
                'login.html',
                {'message': 'Login Successful'}
            )

        return render(
            request,
            'login.html',
            {'message': 'Invalid Username or Password'}
        )

    return render(request, 'login.html')
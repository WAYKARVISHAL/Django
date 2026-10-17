from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sales(request):
    return render(request, 'sales.html')

def services(request):
    return render(request, 'services.html')
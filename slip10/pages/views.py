from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def admissions(request):
    return render(request, 'pages/admissions.html')

def news(request):
    return render(request, 'pages/news.html')
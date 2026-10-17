from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def friends(request):
    return render(request, 'friends.html')

def posts(request):
    return render(request, 'posts.html')

def requests(request):
    return render(request, 'requests.html')
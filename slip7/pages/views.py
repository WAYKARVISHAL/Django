from django.shortcuts import render
from django.contrib.auth import authenticate

def home(request):
    return render(request, 'pages/home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            return render(request, "pages/login.html", {
                "message": "success"
            })
        else:
            return render(request, "pages/login.html", {
                "message": "Invalid username or password"
            })

    return render(request, "pages/login.html")
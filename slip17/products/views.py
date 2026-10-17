from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    return render(request,'home.html')

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})
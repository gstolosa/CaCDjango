from django.shortcuts import render
# from .models import Product
from .models import Category


# Create your views here.

# def products(request):
#     products = Product.objects.all()
#     return render(request, "products/products.html", {'products': products})

def products(request):
    categories = Category.objects.all()
    return render(request, "products/products.html", {'categories': categories})

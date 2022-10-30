from django.shortcuts import render
from .models import Category

def products(request):
    categories = Category.objects.all().order_by('title')
    return render(
        request, 
        "products/products.html", 
        {'categories': categories}
    )

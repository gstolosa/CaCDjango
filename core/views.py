from django.shortcuts import render, redirect
from products.models import Product
from core.forms import ProductForm
from django.views import View

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def administracion(request):
    products= Product.objects.all()
    return render(request, "administracion/index.html", {'products':products})


class ProductoView(View):
    form_class=ProductForm
    template_name= 'administracion/productos/crear.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *arg, **kwargs):
        form= self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('administracion')
        return render(request, self.template_name, {'formulario':form})
        


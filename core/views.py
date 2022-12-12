from django.shortcuts import render, redirect
from products.models import Product,Category
from core.forms import ProductForm, CategoryForm
from django.views import View
from django.http import HttpResponse

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def administracion(request):
    products= Product.objects.all()
    return render(request, "administracion/index.html", {'products':products})

def indexcat(request):
    categorias= Category.objects.all()
    return render(request, "administracion/categorias/indexcat.html", {'categorias':categorias})


class ProductoView(View):
    
    form_class=ProductForm
    template_name= 'administracion/productos/crear.html'

    def get(self, request, *args, **kwargs):
        categorias=Category.objects.all()
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form, 'categorias':categorias})

    def post(self, request, *arg, **kwargs):
        categorias=Category.objects.all()
        form= self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('administracion')
        return render(request, self.template_name, {'formulario':form, 'categorias':categorias})

def prod_editar(request, id_prod):
    producto= Product.objects.get(id=id_prod)
    formulario = ProductForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('administracion')                
    return render(request, 'administracion/productos/editar.html',{'formulario':formulario, 'id_prod':id_prod})

def prod_eliminar(request,id):
    producto=Product.objects.get(id=id)
    producto.delete()
    return redirect('administracion')


class CategoryView(View):
    form_class=CategoryForm
    template_name= 'administracion/categorias/crear_cat.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *arg, **kwargs):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexcat')
        return render(request, self.template_name, {'formulario':form})

def cat_editar(request, id_cat):
    categoria= Category.objects.get(id=id_cat)
    formulario = CategoryForm(request.POST or None, instance=categoria)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('indexcat')                
    return render(request, 'administracion/categorias/editar_cat.html',{'formulario':formulario, 'id_cat':id_cat})

def cat_eliminar(request,id):
    categoria=Category.objects.get(id=id)
    categoria.delete()
    return redirect('indexcat')
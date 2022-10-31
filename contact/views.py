from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Formulario Válido<br>TODO: Grabar en la BBDD")
        else:
            return render(request, 'contact/contact.html', {'form': form})
from django.forms import ModelForm
from django import forms
from .models import Contact

import re

class ValidateField():
    def is_valid_name(name):
        exp = re.compile(r"^[a-zA-Z áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñÑ']{1,40}$")
        return exp.match(name)

    def is_valid_phone(phone):
        exp = re.compile(r"^[0-9]{10}$")
        return exp.match(phone)

    def is_valid_email(email):
        exp = re.compile(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]+$")
        return exp.match(email)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['fname', 'lname', 'phone', 'email', 'message']
        labels = {
            'fname': 'Nombre',
            'lname': 'Apellido',
            'phone': 'Celular',
            'email': 'Correo Electrónico',
            'message': 'Mensaje',
        }

    def clean_fname(self):
        fname = self.cleaned_data.get("fname")
        if not ValidateField.is_valid_name(fname):
            raise forms.ValidationError("El nombre solo puede contener letras")
        else:
            return fname

    def clean_lname(self):
        lname = self.cleaned_data.get("lname")
        if not ValidateField.is_valid_name(lname):
            raise forms.ValidationError("El apellido solo puede contener letras")
        else:
            return lname

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not ValidateField.is_valid_phone(phone):
            raise forms.ValidationError("El celular debe contener 10 dígitos")
        else:
            return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not ValidateField.is_valid_email(email):
            raise forms.ValidationError("La dirección de correo electrónico no es válida")
        else:
            return email

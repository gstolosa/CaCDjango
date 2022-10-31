from django import forms
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


class ContactForm(forms.Form):
    
    fname = forms.CharField(
        label="Nombre",
        max_length=40,
        widget=forms.TextInput()
    )

    lname = forms.CharField(
        label="Apellido",
        max_length=40,
        widget=forms.TextInput()
    )

    phone = forms.CharField(
        label="Celular",
        max_length=10,
        widget=forms.TextInput()        
    )
    
    email = forms.EmailField(
        label="Correo Electrónico",
        max_length=40,
        widget=forms.EmailInput()        
    )
    
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea()
    )
    
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

        
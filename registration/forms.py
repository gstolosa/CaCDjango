from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text = "Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    #Validar si el mail ya existe    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("El correo ya se encuentra en uso, reintente con otro e-mail")
        return email
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-4', 'rows':4, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3','placeholder':'enlace'}),       
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    
    class Meta:
        model = User
        fields = ['email']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El correo ya se encuentra en uso, reintente con otro e-mail")
        return email
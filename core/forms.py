from django import forms
from products.models import Product,Category

class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields= ['title', 'description', 'image', 'category']
    
    title=forms.CharField(
        label='Titulo',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    description=forms.CharField(
        label='Descripcion',
        widget=forms.Textarea(attrs={'class':'form-control'})
    )

    image=forms.FileField(
        label='Imagen',
        widget=forms.FileInput(attrs={'class':'form-control'})
    )

    category=forms.ModelChoiceField(
        label='Categoria',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        to_field_name= "title"
        )

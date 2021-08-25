from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       =   forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Your description'}))
    descripcion =   forms.CharField(required=False)
    price       =   forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = ['title', 'descripcion','price']
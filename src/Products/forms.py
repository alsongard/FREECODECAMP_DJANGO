from django import forms
from .models import Products
class ProductForms(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'category',
            'title',
            'description',
            'price',
            'summary'
        ]

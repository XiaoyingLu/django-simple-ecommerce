from dataclasses import fields
from importlib.metadata import files
from turtle import title
from django import forms

from cart.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'available_colours',
            'available_sizes',
        ]

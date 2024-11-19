from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'item_id': 'Item ID',
            'name': 'Name',
            'sku': 'Stock Keeping Unit',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'item_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 1'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g shoe'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g W1234'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 27.35'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 5'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g ROS Org'}),


        }
from django import forms
from .models import Supplier, Product, SaleOrder

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'stock_quantity', 'supplier']

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = ['product', 'quantity', 'status']

from .models import StockMovement

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['product', 'quantity', 'movement_type', 'notes']

def clean_phone(self):
    phone = self.cleaned_data['phone']
    if not phone.isdigit() or len(phone) != 10:
        raise forms.ValidationError("Enter a valid 10-digit phone number.")
    return phone

def clean_price(self):
    price = self.cleaned_data['price']
    if price <= 0:
        raise forms.ValidationError("Price must be greater than 0.")
    return price

def clean(self):
    cleaned_data = super().clean()
    product = cleaned_data.get('product')
    quantity = cleaned_data.get('quantity')
    if product and quantity and quantity > product.stock_quantity:
        raise forms.ValidationError("Insufficient stock for this product.")
    return cleaned_data


import imp
from django import forms
from .models.product import Products
from .models.orders import Order

class ProductCreate(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class OrdersViews(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


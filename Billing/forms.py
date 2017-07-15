from django import forms
from django.forms import ModelForm
from django.contrib.auth import (authenticate , get_user_model , login , logout )

from .models import Item

User = get_user_model()

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['Name', 'Product' , 'Price' , 'Quantity' , 'Order' , 'Date']


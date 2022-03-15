from django import forms
from ci_order.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['first_name','last_name','email','address','country','state','city']
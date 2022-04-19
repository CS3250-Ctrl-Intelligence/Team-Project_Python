from django import forms
from ci_order.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['first_name','last_name','email','address','zipcode','state','city']
    
class RefundForm(forms.Form):
    order_num = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows':4
    }))

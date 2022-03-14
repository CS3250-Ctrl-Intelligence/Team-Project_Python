from django import forms
from ci_account.models import Account

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields=['first_name','last_name','email','password']
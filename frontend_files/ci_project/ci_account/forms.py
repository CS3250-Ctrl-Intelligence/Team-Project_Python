from django import forms
from ci_account.models import Account
 
class RegistrationForm(forms.ModelForm):
   password = forms.CharField(widget= forms.PasswordInput(attrs={
       'placeholder': 'Enter Password'
       # use the format below to customize this SPECIFIC form field with css
       # 'class':'class-name'
   }))
   password_confirmation = forms.CharField(widget= forms.PasswordInput(attrs={
       'placeholder': 'Reenter Password'
   }))
 
 
   class Meta:
       model = Account
       fields=['first_name','last_name','email','password']
 
   # apply css to ALL fields in form
   # def __init__(self,*args,**kwargs):
   #     super(RegistrationForm,self).__init__(*args,**kwargs)
   #     self.fields['first_name'].widget.attrs['placeholder']='Enter first name'
   #     for field in self.fields:
   #         self.fields[field].widget.attrs['class']='class-name'
 
   def clean(self):
       cleaned_data = super(RegistrationForm,self).clean()
       password_1 = cleaned_data.get('password')
       password_2 = cleaned_data.get('password_confirmation')
 
       if password_1 != password_2:
           raise forms.ValidationError(
               "Password does not match!"
           )
 
 
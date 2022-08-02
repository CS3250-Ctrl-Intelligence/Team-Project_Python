from django import forms
from ci_account.models import Account,UserProfile
 
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput(attrs={
       'class': 'form-control',       
       'placeholder': 'Password',
       # use the format below to customize this SPECIFIC form field with css
       # 'class':'class-name'
    }))
    password_confirmation = forms.CharField(widget= forms.PasswordInput(attrs={
       'class': 'form-control',       
       'placeholder': 'Confirm Password',
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',       
       'placeholder': 'First Name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',       
       'placeholder': 'Last Name',
    }))
    email =forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',       
       'placeholder': 'Email',

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
 
class UserForm(forms.ModelForm):
   class Meta:
      model = Account
      fields=('first_name','last_name','email')
   
   
   def __init__(self,*args,**kwargs):
      super(UserForm,self).__init__(*args,**kwargs)
      for field in self.fields:
         self.fields[field].widget.attrs['class']='form-control'

class UserProfileForm(forms.ModelForm):
   profile_picture = forms.ImageField(required=False, error_messages={'invalid':("Images only")}, widget= forms.FileInput)
   class Meta:
      model = UserProfile
      fields =('address','city','state','zip','profile_picture')

   def __init__(self,*args,**kwargs):
      super(UserProfileForm,self).__init__(*args,**kwargs)
      for field in self.fields:
         self.fields[field].widget.attrs['class']='form-control'

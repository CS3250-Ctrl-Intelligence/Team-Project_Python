from django.shortcuts import render
from ci_account.forms import RegistrationForm
# Create your views here.


def register(request):
    form = RegistrationForm()

    return render(request,'register.html',{'form':form})

def login(request):

    return render(request,'login.html')    

def logout(request):

    return render(request,'logout.html')
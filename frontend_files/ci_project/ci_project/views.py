from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def contactUs(request):
    return render(request,'contactUs.html')



def about(request):
    return render(request,'about.html')


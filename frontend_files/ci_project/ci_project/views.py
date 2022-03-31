from django.shortcuts import render

from ci_shop.models import Product

def home(request):
    data=Product.objects.filter(featured =True).order_by('-id')
    return render(request,'home.html',{'data':data})


def contactUs(request):
    return render(request,'contactUs.html')



def about(request):

    return render(request,'about.html',)


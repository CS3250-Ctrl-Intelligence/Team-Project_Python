from django.shortcuts import render
from django.core.mail import send_mail
from ci_shop.models import Product

def home(request):
    data=Product.objects.filter(featured =True).order_by('-id')
    return render(request,'home.html',{'data':data})


def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('input-name')
        email = request.POST.get('input-email')
        subject = request.POST.get('input-subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''\nNew message: {}\nFrom: {} {}'''.format(data['message'], data['name'], data['email'])
        send_mail(data['subject'], message, "bounces+28347242@em9511.ctrlintel.shop", ['controlintel23@gmail.com '])
    return render(request,'contact.html')



def about(request):

    return render(request,'about.html',)


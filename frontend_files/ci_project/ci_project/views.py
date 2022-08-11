from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.html import strip_tags
from ci_shop.models import Product
from django.template.loader import render_to_string

def home(request):
    data=Product.objects.filter(featured =True).order_by('-id')
    return render(request,'home.html',{'data':data})


def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('input-name')
        email = request.POST.get('input-email')
        subject = request.POST.get('input-subject')
        message = request.POST.get('message')

        context = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        
        html_message = render_to_string('contact_msg.html', context)
        plain_text = strip_tags(html_message)

        send_mail(context['subject'], plain_text, "bounces+28347242@em9511.ctrlintel.shop", ['controlintel23@gmail.com'], html_message=html_message)
    return render(request,'contact.html')



def about(request):

    return render(request,'about.html',)


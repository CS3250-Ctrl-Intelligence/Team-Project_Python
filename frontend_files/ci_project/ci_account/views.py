from email.message import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# Email verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from ci_account.forms import RegistrationForm
from ci_account.models import Account
from ci_cart.views import _cart_session
from ci_cart.models import Cart,CartItem


def register(request):
   # handle submission
    if request.method =='POST':
       # request.POST contain all the fields' values
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # split email and assign the first part to username
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name = first_name, last_name = last_name,username = username,email=email,password= password)
            user.save()

            # implement user activation
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accountVerification.html',{
                    'user' :user,
                    'domain' :current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)

            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            #messages.success(request,'Please check your email to verify your account.')
            # redirect to login page
            return redirect('/account/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})
 
def login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
 
        user = auth.authenticate(email=email,password=password)
        #if user exist, log in
        if user is not None:
            try:
                # create cart table from session id, go to except block if there is no item when we're logged in
                cart = Cart.objects.get(cart_id=_cart_session(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    
                    for item in cart_item:
                        item.user = user
                        item.save()
            except:
                pass
            auth.login(request,user)
            #messages.success(request,"You're now logged in")
            # go to home page
            return redirect('home')
        else:
            # print out error message
            messages.error(request,"Invalid login credentials")
            # stay in login page
            return redirect('login')
    return render(request,'login.html')   
 
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,"You are logged out")
    return redirect('login')


def activate(request,uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError,ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation! Your account is activated')
        return redirect('login')
    else:
        messages.error(request,'Invalid activation link')
        return redirect('register')
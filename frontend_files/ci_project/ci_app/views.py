from django.shortcuts import render
from ci_app.models.team_member import TeamMember
from ci_app.models.product import Product
from ci_app.models.customer import Customer
from ci_app.models.customer_order import CustomerOrder
# Create your views here.

def about(request):
    team_list = TeamMember.objects.order_by('first_name')
    team_dict = {'team_member': team_list}
    return render(request,'about.html',team_dict)


def home(request):
    return render(request,'home.html')

def store(request):
    item_list = Product.objects.order_by('product_id')
    item_dict = {'item_inv': item_list}
    return render(request,'store.html',item_dict)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = CustomerOrder.objects.get_or_create(customer = customer)
        items = order.customerorderitem_set.all()
    else:
        items = []
        order={'get_cart_total':0,'get_cart_items':0}
    cart_dict={'order_items':items,'order':order}
    return render(request,'cart.html',cart_dict)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = CustomerOrder.objects.get_or_create(customer = customer)
        items = order.customerorderitem_set.all()
    else:
        items = []
        order={'get_cart_total':0,'get_cart_items':0}
    checkout_dict={'order_items':items,'order':order}
    return render(request,'checkout.html',checkout_dict)

def contactUs(request):
    return render(request,'contactUs.html')

def history(request):
    return render(request,'history.html')

def recommend(request):
    return render(request,'recommend.html')

def refund(request):
    return render(request,'refund.html')
from unicodedata import name
from django.urls import path

from ci_cart import views

#/shop/cat_slug/prod_slug
urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('cart/cart_add/<int:product_id>/',views.cart_add, name ='cart_add'),
    path('cart/cart_remove/<int:product_id>/',views.cart_remove, name ='cart_remove'),
    path('cart/cart_item_remove/<int:product_id>/',views.cart_item_remove, name ='cart_item_remove'),
    path('cart/checkout/',views.checkout, name="checkout")
]



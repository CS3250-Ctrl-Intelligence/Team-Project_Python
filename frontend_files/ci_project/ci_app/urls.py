from django.urls import path
from ci_app import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('store/',views.store,name='store'),
    path('contactUs/',views.contactUs,name='contactUs'),
    path('history/',views.history,name='history'),
    path('recommend/',views.recommend,name='recommend'),
    path('refund/',views.refund,name='refund'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout, name='checkout'),
]

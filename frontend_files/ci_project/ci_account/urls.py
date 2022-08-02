from django.urls import path

from ci_account import views


urlpatterns = [
   path('register/',views.register,name="register"),
   path('login/',views.login,name="login"),
   path('logout/',views.logout,name="logout"),
   path('activate/<uidb64>/<token>/',views.activate,name="activate"),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('my_orders/',views.my_orders,name='my_orders'),
   path('order_detail/<int:order_id>/',views.order_detail,name='order_detail'),
   path('my_orders/refund_request/<int:order_id>/',views.refund_request, name ='refund_request'),
   path('edit_profile/',views.edit_profile,name='edit_profile'),
]



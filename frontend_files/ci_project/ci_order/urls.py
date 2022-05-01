from django.urls import path
from ci_order import views
urlpatterns = [
    path('place_order/',views.place_order, name = 'place_order'),
    path('payments/',views.payments,name='payments'),
    path('order_complete/',views.order_complete, name='order_complete'),
    path('request-refund/',views.RequestRefundView.as_view(),name="request-refund"),
]
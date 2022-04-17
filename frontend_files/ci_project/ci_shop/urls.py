from django.urls import path

from ci_shop import views


#/shop/cat_slug/prod_slug
urlpatterns = [
    path('shop/',views.shop,name='shop'),
    path('shop/',views.shop, name= "prods_by_cat"),
    path('shop/<slug:product_slug>/',views.product_detail, name= "product_detail"),
]



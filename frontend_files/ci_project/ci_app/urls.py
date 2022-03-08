from django.urls import path
from ci_app import views


urlpatterns = [
    path('about/',views.about,name='about'),
    path('',views.home,name='home')
]

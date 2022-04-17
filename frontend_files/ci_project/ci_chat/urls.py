from django.urls import path
from ci_chat.views import chatbot

urlpatterns = [
    path('',chatbot.as_view(),),
]
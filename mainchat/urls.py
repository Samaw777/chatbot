from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='mainchat-index'),
    path('home/', views.home, name='mainchat-home'),
    path('output/', views.output, name='mainchat-output'), 
    path('chatbot_response/', csrf_exempt(views.chatbot_response), name='chatbot-response'),
]

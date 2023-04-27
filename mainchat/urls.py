from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.homepage, name='mainchat-homepage'),
    path('home/', views.home, name='mainchat-home'),
    path('output/', views.output, name='mainchat-output'),
    path('login/', views.login, name='mainchat-login'),
    path('signup/', views.signup, name='mainchat-signup'), 
    path('afterlogin/', views.afterlogin, name='mainchat-afterlogin'),
    path('chatbot_response/', csrf_exempt(views.chatbot_response), name='chatbot-response'),
    path('chatpaneltest', views.chatpaneltest, name='chatpaneltest'),
    path('about', views.about, name='about'),
    path('get_Response', views.get_Response, name='get_Response')
]

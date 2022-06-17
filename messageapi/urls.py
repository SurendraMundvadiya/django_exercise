from django.urls import path
from . import views
from . import auth

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', auth.CustomAuthToken.as_view()),
    path('logout/', auth.Logout.as_view()),
    path('send_message/', views.sendmessage),
    path('get_messages/', views.getmessages),
]

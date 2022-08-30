from django.urls import path
from .views.login import MyTokenObtainPairView
from .views import message, login


urlpatterns = [
    path('', login.index),
    path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('register/', login.adduser),
    path('logout/', login.logout_request, name='logout'),
    path('newmessage', message.newmessage, name='add'),
    path('messages', message.messages, name='getall'),
    path('messages/<id>', message.messages, name='getone'),
    path('unread', message.unread, name='getunread'),
    path('delmessage/<id>', message.delmessage, name='del'),
  
]


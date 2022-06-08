from django.urls import path
import rest_framework.authtoken.views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', rest_framework.authtoken.views.obtain_auth_token),
    path('users', views.UserList.as_view()),
    path('channels', views.ChannelList.as_view()),
    path('channels/<int:channel_id>/messages', views.MessageList.as_view()),
]
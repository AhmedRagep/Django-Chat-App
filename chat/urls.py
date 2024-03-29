from django.urls import path
from . import views

app_name='chat'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('check', views.check, name='check'),
    path('send', views.send, name='send'),
    path('getmessages/<str:room>/', views.getmessages, name='getmessages'),

    path('test',views.test,name='test')
    
]

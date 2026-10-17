from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('friends/', views.friends, name='friends'),
    path('posts/', views.posts, name='posts'),
    path('requests/', views.requests, name='requests'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admissions/', views.admissions, name='admissions'),
    path('news/', views.news, name='news'),
]
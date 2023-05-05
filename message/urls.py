from django.urls import path
from . import views

urlpatterns = [
    path('', views.one, name='one'),
    path('home/', views.home, name='home'),
    path('dom/', views.dom, name='dom'),
    path('form/', views.data_users, name='data_users'),
]

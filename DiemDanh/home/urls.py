from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('/', views.home, name='home'),
    # path('index/', include('index.urls')),
    # path('login/', include('login.urls')),

    path('', views.get_home, name='home'),
    path('index/', views.get_home, name='home'),
    path('login/', views.loginPage, name='login'),
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('/', views.home, name='home'),
    # path('index/', include('index.urls')),
    # path('login/', include('login.urls')),

    path('', views.get_home, name='home'),
    path('login/', views.get_login, name='login'),
    path('history/', views.get_history, name='history'),
    path('profile/', views.get_profile, name='profile'),
    path('profile-edit/', views.get_profileEdit, name='profile-edit'),
    

]
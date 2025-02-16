"""
URL configuration for DiemDanh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', home.get_home, name='home'),
    # path('login/', home.get_login, name='login'),
    # path('courses/', home.get_course, name='courses'),

  
    path('admin/', admin.site.urls),
    path('login/', home.get_login, name='login'),
    path('', home.get_home, name='home'),
    path('profile/', home.get_profile, name='profile'),
    path('profile-edit/', home.get_profileEdit, name='profile-edit'),
    path('history/', home.get_history, name='history'),
    path('face_recognition/', home.get_face_recognition, name='face_recognition'), 
    path('video_feed/', home.video_feed, name="video_feed"),
]
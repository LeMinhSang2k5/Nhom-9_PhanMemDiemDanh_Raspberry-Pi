from django.contrib import admin
from django.urls import path, include
from . import views
from home.views import video_feed

urlpatterns = [
    # path('/', views.home, name='home'),
    # path('index/', include('index.urls')),
    # path('login/', include('login.urls')),

    path('', views.get_home, name='home'),
    path('login/', views.get_login, name='login'),
    path('history/', views.get_history, name='history'),
    path('profile/', views.get_profile, name='profile'),
    path('profile-edit/', views.get_profileEdit, name='profile-edit'),
    path('face_recognition/', views.get_face_recognition, name='face_recognition'),
    path('video_feed/', views.video_feed, name="video_feed"),
    path('lich-su-diem-danh/', lich_su_diem_danh, name="lich_su_diem_danh"),
]
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def get_home(request):
    return render(request, 'home/home.html')


# dat ten get_ cho no dong bo voi cac ham khac
def get_login(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pw')

        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home') 
                return redirect(next_url)
            else:
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
        else:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin')

    return render(request, 'home/loginPage.html')

def get_course(request):
    return render(request, 'home/courses.html')

def get_profile(request):
    return render(request, 'home/profile.html')

def get_history(request):
    return render(request, 'home/history.html')

    
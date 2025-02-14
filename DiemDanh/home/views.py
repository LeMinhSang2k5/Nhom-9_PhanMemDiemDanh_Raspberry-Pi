from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import history_attendance,teachers

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

                # Kiểm tra quyền của user
                if user.is_superuser:
                    return redirect('/admin/')  # Admin vào trang admin
                elif hasattr(user, 'userprofile') and user.userprofile.is_teacher:
                    return redirect('/courses/')  # Giáo viên vào trang course
                else:
                    next_url = request.GET.get('course', 'home')  # User thường về home
                    return redirect(next_url)
            else:
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
        else:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin')

    return render(request, 'home/loginPage.html')

def get_course(request):
    today = datetime.today()
    context = {
        'current_month': today.strftime("%B %Y"),
        'current_day': today.day,
    }
    return render(request, 'home/courses.html', context)

def get_profile(request):
    teacher = teachers.objects.all()  # Lấy toàn bộ danh sách giáo viên
    return render(request, 'home/profile.html', {'teacher': teacher})

def get_history(request):
    history = history_attendance.objects.all()  # Lấy tất cả bản ghi từ database
    return render(request, 'home/history.html', {'history': history})

    
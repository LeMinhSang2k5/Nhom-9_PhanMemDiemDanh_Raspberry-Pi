from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def get_home(request):
    return render(request, 'home/index.html')

def get_login(request):
    return render(request, 'home/loginPage.html')

# def get_login(request, id):
#   DiemDanh_login = login.objects(id = id)
#   template = loader.get_template('home/loginPage.html')
#   context = {
#     'DiemDanh_login': login,
#   }
#   return HttpResponse(template.render(context, request))

# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('home')
#     else: messages.info(request, 'Username or password is incorrect')
#     context = {}
#     return render(request, 'loginPage.html', context)
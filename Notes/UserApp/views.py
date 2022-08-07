from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from UserApp.models import note_model
from postNote.models import post_model


def home(request):
    dic = {
        'data': post_model.objects.filter(post_user=request.user)
    }
    return render(request, 'home.html',dic)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_page(request):
    # if user already login
    if request.user.is_authenticated:
        return redirect('/')
    # when method only post
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        try:
            user = User.objects.create_user(username=username, password=password,
                                            first_name=name, email=email)
        except:
            print('Error')
    return render(request, 'signup.html')

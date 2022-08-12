from datetime import datetime
from traceback import print_tb
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import models
from .forms import todo_form
from django.core.paginator import Paginator
from .models import post


def HomePage(request):
    dic = dict()
    try:
        pagedata = post.objects.filter(user=request.user).order_by('dt')[::-1]
        paginator = Paginator(pagedata, 5)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        dic = {
            'data': post.objects.filter(user=request.user),
            'finalpage': page
        }
        if request.method == 'POST':
            SavePost = post()
            SavePost.user = request.user
            SavePost.todo = request.POST.get('todo')
            SavePost.dt = datetime.now()
            if len(SavePost.todo) > 0:
                SavePost.save()
                return redirect('/')
    except:
        pass
    return render(request, 'home.html', dic)


def login_page(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        print(user, password)
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    if request.user.is_authenticated:  # alredy login
        return redirect('/')
    return render(request, 'login.html')


def logout_page(request):
    if User.is_authenticated:  # alredy login
        logout(request)
        return redirect('/')


def signup_page(request):
    if request.method == 'POST':
        user = User
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        root = authenticate(request=request, username=user.username,
                            password=user.password, email=user.email)
        if root is None:
            if len(user.username) > 2:
                User.objects.create_user(username=user.username,
                                         password=user.password, email=user.email)
            return redirect('/')
        else:
            return HttpResponse('alredy exits')
    return render(request, 'signup.html')


def del_post(request, val):
    p = post.objects.get(id=val).delete()
    return redirect('/')


def edit_post(request, val):
    p = post.objects.get(id=val)
    if request.method == 'POST':
        if p.user == request.user:
            p.todo = request.POST.get('todo')
            p.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': p})

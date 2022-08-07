from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from postNote.forms import post_form
from postNote.models import post_model

# Create your views here.


def post_page(request, naam):
    if request.user is not authenticate:
        return redirect('login_page')
    if request.method == 'POST':
        user = post_model()
        user.post_user = request.user
        user.post_title = request.POST.get('post_title')
        user.post_desc = request.POST.get('post_desc')
        user.save()
    dic = {
        'form': post_form()
    }
    return render(request, 'post.html', dic)


def post_del(request, val):
    p = post_model.objects.get(id=val).delete()
    return redirect('/')


def post_update(request, val):
    if request.user is not authenticate:
        return redirect('login_page')
    p = post_model.objects.get(pk=val)
    q = post_form(instance=p)
    if request.method == 'POST':
        ob = post_form(request.POST, instance=p)
        if ob.is_valid():
            ob.save()
            return redirect('/')
    dic = {
        'val': q
    }
    return render(request, 'update.html', dic)

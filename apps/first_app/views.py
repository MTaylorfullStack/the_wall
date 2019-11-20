from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import random
from .models import *

def index(request):
    context = {
        'all_messages': Message.objects.all()
    }
    return render(request, "first_app/index.html", context)


def reset(request):
    request.session.flush()
    return redirect('/')

def add_user(request):
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        print("hello world")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        User.objects.create(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
    return redirect('/')

def add_message(request):
    posted_by = User.objects.filter(name=request.POST['poster'])
    if len(posted_by) > 0:
        errors = Message.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        Message.objects.create(message=request.POST['mess'], poster=posted_by[0])
        print("message created!")
    else:
        return redirect('/')
    return redirect('/')

def one_user(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user' : User.objects.get(id=user_id),
        'all_user_messages': user.messages.all()
    }
    return render(request, 'first_app/one.html', context)


def destroy(request, mess_id):
    mess = Message.objects.get(id=mess_id)
    mess.delete()
    return redirect('/')

# Create your views here.

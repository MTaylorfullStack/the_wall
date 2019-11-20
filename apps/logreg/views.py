from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "logreg/index.html")


def add_user(request):
    errors = User.objects.basic_validator(request.POST)
    print("This needs to be here!")
    if len(errors) > 0:
        print("There were errors here")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    if request.POST['password'] == request.POST['confirm_password']:
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password = request.POST['password'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/wall')
    else:
        return redirect('/')


def login(request):
    #getting a user with email from form
    logged_user = User.objects.filter(email=request.POST['email'])
    if logged_user[0]:
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0].first_name
            request.session['id'] = logged_user[0].id
            return redirect('/wall')
        
    else:
        return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')
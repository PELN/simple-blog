from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
# from django.contrib.auth.decorators
from .utils import random_string

# from .models import *

# Create your views here.

def login(request):
    # now the context exists but it is empty by default
    context = {}

    if request.method == 'POST':
        # request.POST is a dictionary, you need a key to get the value
        user = authenticate(request, 
            username=request.POST['user'], 
            password=request.POST['password'])
        # check if user is real
        if user:
            # if user is in the system, redirect them
            dj_login(request, user)
            #context = {'user':request.POST['user']} - useless, not passing the context to the return
            return HttpResponseRedirect(reverse ('blogapp:index'))
        else:
            # send error message
            # context = {'error':'Username or password is wrong.'}
            context['error'] = "Username or password is wrong."

    # don't receive a post request, render template as default
    # request and url are required arguments, context is not require
    return render(request, 'loginapp/login.html', context)

def logout(request):
    dj_logout(request)
    # redirect user if they logout
    return HttpResponseRedirect(reverse ('loginapp:login'))



def signup(request):
    if User.is_authenticated:
        dj_logout(request)

    if request.method == 'POST':
        # fill it out with what i need on the way
        context = {}
        # use if not - can easily go out, if it is wrong
        if not request.POST['password'] == request.POST['confirmPassword']:
            #if they dont match, put an error message in the context
            context['error'] = "Passwords do not match."
            # if it is wrong, render the template and send the context
            return render(request, 'loginapp/signup.html', context)
        #check if the list of users is empty or not - use len
        if len(User.objects.filter(username = request.POST['user'])) > 0:
            # if the user already exists, send new error message
            context['error'] = 'Username already exists'
            return render(request, 'loginapp/signup.html', context)

        # create user
        user = User.objects.create_user(request.POST['user'],password=request.POST['password'])
        user.save()
        dj_login(request, user)
        return HttpResponseRedirect(reverse ('blogapp:index'))
        

    # if it is not a post (then it is a get) it should just show the signup form
    return render(request, 'loginapp/signup.html')


def password_reset(request):
    context = {}
    # user should provide the username
    if request.method == 'POST':
    # generate a random string for password and show it in the console 

        # filter can return many things, it is a list - test if the list is empty
        users = User.objects.filter(username=request.POST['user'])
        # if user exists, grab the user
        if users:
            user = users[0]
            new_password = random_string()
            user.set_password(new_password)
            user.save()
            print(f'*********** User {user} change password to {new_password}')
            return HttpResponseRedirect(reverse('loginapp:login'))

        # if the list is empty, send back an error
        else:
            context['error'] = "No such username"

    return render(request, 'loginapp/password_reset.html', context)


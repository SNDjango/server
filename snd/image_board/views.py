from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.conf import settings

def index(request):
    return render(request, 'index.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect_to_login('profile', login_url='login_page')
    else:
        return render(request, 'profile.html')


def login_page(request):
    if(request.method == 'POST'):
        name = request.POST['user']
        pwd = request.POST['pwd']

        user = authenticate(username=name, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'error_login.html')

    else:
        return render(request, 'login.html')


def signup(request):
    if(request.method == 'POST'):
        name = request.POST['user']
        email = request.POST['email']
        pwd = request.POST['pwd']

        user = User.objects.create_user(name, email, pwd)
        return redirect('index')

    else:
        return render(request, 'signup.html')


def logout_page(request):
    logout(request)
    return redirect('index')

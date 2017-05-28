from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def index(request):
    return render(request, 'index.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect_to_login('profile', login_url='login_page')
    else:
        return render(request, 'profile.html')

def view_my_posts(request):
     return render(request,'myposts.html')

#favorites to be implemented in the future
def view_my_favorites(request):
    return render(request, 'favorites.html')

def create_post(request):
    return render(request, 'createpost.html')


def login_page(request):
    if(request.method == 'POST'):
        name = request.POST['user']
        if not User.objects.filter(username=name).exists():
            return render(request, 'login.html', {'error_user': 'user does not exist'})
        pwd = request.POST['pwd']
        user = authenticate(username=name, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_pwd': name})

    else:
        return render(request, 'login.html')


def signup(request):
    if(request.method == 'POST'):
        name = request.POST['user']
        if User.objects.filter(username=name).exists():
            return render(request, 'signup.html', {'error_user': 'user already exists'})

        email = request.POST['email']
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'signup.html', {'error_email': 'email not valid', 'name': name})

        pwd = request.POST['pwd']
        if len(pwd) < 8:
            return render(request, 'signup.html', {'error_pwd': 'password not valid', 'name': name, 'email': email})

        user = User.objects.create_user(name, email, pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def logout_page(request):
    logout(request)
    return redirect('index')

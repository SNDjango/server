from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from PIL import Image

from .models import ContentItem


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
    if not request.user.is_authenticated:
        return redirect('index')

    return render(request, 'createpost.html')


def login_page(request):
    if(request.method == 'POST'):
        name = request.POST['user']
        pwd = request.POST['pwd']
        user = authenticate(username=name, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html',{'error_message': 'Invalid login'})

    else:
        return render(request, 'login.html')


def signup(request):
    if(request.method == 'POST'):
        name = request.POST['user']
        email = request.POST['email']
        pwd = request.POST['pwd']

        user = User.objects.create_user(name, email, pwd)
        return redirect('login_page')

    else:
        return render(request, 'signup.html')


def logout_page(request):
    logout(request)
    return redirect('index')


def upload(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to be authenticated to create a new post.')
        return redirect('index')

    if request.method == 'POST' and request.FILES['file'] and request.user:
        submitted_title = request.POST.get('title', '<<post error>>')
        submitted_description = request.POST.get('description', '<<post error>>')
        submitted_file = request.FILES['file']
        try:
            if submitted_file.size > 5242880:
                messages.error(request, 'File is too large. Max is 5MB')
                raise ValueError("File is too large.")
            trial_image = Image.open(submitted_file)
            trial_image.verify()
        except:
            messages.error(request, 'File validation failed.')
            return redirect('create_post')

        try:
            submitted_item = ContentItem(title=submitted_title, description=submitted_description, image=submitted_file, uploaded_by=request.user)
            submitted_item.save()
        except:
            messages.error(request, 'Could not write to Database')
            return redirect('create_post')
        messages.success(request, 'Post created successfully.')
        return redirect('create_post')
    else:
        messages.error(request, 'Bad request.')
        return redirect('create_post')


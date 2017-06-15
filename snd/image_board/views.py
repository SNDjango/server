from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from PIL import Image
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from PIL import Image
from .models import ContentItem
from .models import Profile
from .models import Like
from .models import Hashtag, ContentHashTag
from django.db import IntegrityError

def index(request):
    if(request.method == 'POST'):
        views = int(request.POST['views'])+2
    else:
        views = 2
    all_posts = ContentItem.objects.all().order_by('-upload_date')[:views]
    return render(request, 'index.html', {'all_posts': all_posts, 'view_more': views})


class IndexView(generic.ListView):
    template_name = 'profile.html'

    def get_queryset(self):
        return Profile.objects.all()


class UserUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['personal_info','job_title','department', 'location','expertise', 'user_photo','phone_number','contact_facebook','contact_linkedin','contact_skype']
    template_name = 'user_form.html'
    success_url = reverse_lazy('profile')
    success_message = " Profile was updated successfully"

    def get_object(self):
        return self.request.user.profile

#def profile(request):
 #   if not request.user.is_authenticated:
  #      return redirect_to_login('profile', login_url='login_page')
   # else:
    #    return render(request, 'profile.html')


def view_my_posts(request):
    if request.user.is_authenticated:
        all_posts = ContentItem.objects.filter(uploaded_by = request.user).order_by('-upload_date')
        return render(request, 'myposts.html', {'all_posts': all_posts})
    else:
        return render(request, 'login.html')


#favorites to be implemented in the future
def view_my_favorites(request):
    return render(request, 'favorites.html')


def search(request):
    if not request.user.is_authenticated:
        return redirect_to_login('index', login_url='login_page')
    else:
        return render(request, 'search.html')


def create_post(request):
    if not request.user.is_authenticated:
        return redirect_to_login('create_post', login_url='login_page')

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
            return render(request, 'signup.html', {'error_user': 'Username already taken.'})
        elif name == '':
            return render(request, 'signup.html', {'error_user': 'Username must not be emtpy.'})


        email = request.POST['email']
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'signup.html', {'error_email': 'Invalid email address.', 'name': name})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_email': 'An account with this email address already exists.'})

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


def upload(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to be authenticated to create a new post.')
        return redirect('index')

    submitted_file = request.FILES.get('file', False)

    if request.method == 'POST' and submitted_file and request.user:
        submitted_title = request.POST.get('title', '<<post error>>')
        submitted_description = request.POST.get('description', '<<post error>>')
        tags = request.POST.get('tag-input', '').split(',')
        content_item = None

        try:
            if submitted_file.size > 5242880:
                messages.error(request, 'File is too large. Max is 5MB')
                raise ValueError("File is too large.")

            if submitted_file.size < 1:
                messages.error(request, 'File not valid')
                raise ValueError("File is too small.")
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

        for tag in tags:
            if tag == '':
                continue

            tag = tag[:50]
            try:
                new_tag = Hashtag(hashtag_text=tag)
                new_tag.save()
            except IntegrityError:
                pass

            saved_tag = Hashtag.objects.get(hashtag_text=tag)

            content_hashtag = ContentHashTag(content_id=submitted_item, hashtag_id=saved_tag)
            content_hashtag.save()

        messages.success(request, 'Post created successfully.')
        return redirect('index')
    else:
        messages.error(request, 'Bad request.')
        return redirect('create_post')


def change_password(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to be authenticated to change your password.')
        return redirect('index')

    if not request.method == 'POST':
        return render(request, 'changepassword.html')

    username = request.user

    old_password = request.POST['old_pwd']
    new_password = request.POST['new_pwd']
    repeated_new_password = request.POST['repeat_new_pwd']

    authenticate_user = authenticate(request, username=username, password=old_password)
    if authenticate_user is None:
        return render(request, 'changepassword.html', {'error_pwd': 'Password is wrong.'})

    if new_password != repeated_new_password:
        return render(request, 'changepassword.html', {'error_repeat_pwd': 'Password does not match'})

    if len(new_password) < 8:
        return render(request, 'changepassword.html', {'error_new_pwd': 'password not valid'})

    u = User.objects.get(username__exact=username)
    u.set_password(new_password)
    u.save()

    messages.success(request, 'Password successfully changed.')
    return redirect('login_page')

# https://www.sujinlee.me/blog/django-like-button/
def like_post(request):
    if request.method == 'GET':
        post_id = int(request.GET['post_id'])
        post = ContentItem.objects.get(id=post_id)
        new_like, created = Like.objects.get_or_create(user_id=request.user, content_id=post)
        if not created:
            Like.objects.filter(user_id=request.user, content_id=post).delete()
        likes = post.get_likes()
    return HttpResponse(likes)

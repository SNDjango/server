from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.template import RequestContext
from django.db.models import Count
from PIL import Image
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from PIL import Image
import json
from .models import ContentItem
from .models import Profile
from .models import Like
from .models import Hashtag, ContentHashTag
from .models import Comment
from .models import Downvote, Upvote
from .models import Board, ContentBoard, SubBoard
from django.db import IntegrityError

from .forms import UserForm, ProfileForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import viewsets
from . import serializers


def index(request):
    items_on_page = 1
    max_pages_full = 8

    all_posts = ContentItem.objects.all().order_by('-upload_date')

    paginator = Paginator(all_posts, items_on_page)
    page = request.GET.get('page')

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    if paginator.num_pages > max_pages_full:
        ntl = paginator.num_pages - 1
        nntl = paginator.num_pages - 2
    else:
        ntl = 0
        nntl = 0

    for post in pages:
        tag_ids = list(set(ContentHashTag.objects.filter(content_id=post).values_list('hashtag_id', flat=True)))
        filtered_tags = list(set(Hashtag.objects.filter(pk__in=tag_ids).values_list('hashtag_text', flat=True)))
        post.tags = filtered_tags

    return render(request, 'index.html', {'pages': pages, 'max_pages_full': max_pages_full, 'ntl': ntl, 'nntl': nntl})


class IndexView(generic.ListView):
    template_name = 'profile.html'

    def get_queryset(self):
        return Profile.objects.all()



def profileview(request, id):
    if not request.user.is_authenticated:
        return redirect('login_page')

    try:
        user_id = id
        author = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'There is no such user!')
        return redirect('index')

    if author == request.user:
        return redirect('profile')

    else:
        return render(request,'profile_public.html',{'author':author,'user_id':user_id})



class UserUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['personal_info','job_title','department', 'location','expertise', 'user_photo','phone_number','contact_facebook','contact_linkedin','contact_skype']
    template_name = 'user_form.html'
    success_url = reverse_lazy('profile')
    success_message = " Profile was updated successfully"

    def get_object(self):
        return self.request.user.profile


class PicUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['user_photo']
    template_name = 'user_form.html'
    success_url = reverse_lazy('profile')
    success_message = " Profile was updated successfully"

    def get_object(self):
        return self.request.user.profile


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def view_my_posts(request):
    if request.user.is_authenticated:
        items_on_page = 2
        max_pages_full = 8

        all_posts = ContentItem.objects.filter(uploaded_by = request.user).order_by('-upload_date')

        paginator = Paginator(all_posts, items_on_page)
        page = request.GET.get('page')

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        if paginator.num_pages > max_pages_full:
            ntl = paginator.num_pages - 1
            nntl = paginator.num_pages - 2
        else:
            ntl = 0
            nntl = 0

        for post in pages:
            tag_ids = list(set(ContentHashTag.objects.filter(content_id=post).values_list('hashtag_id', flat=True)))
            filtered_tags = list(set(Hashtag.objects.filter(pk__in=tag_ids).values_list('hashtag_text', flat=True)))
            post.tags = filtered_tags

        return render(request, 'myposts.html', {'pages': pages, 'max_pages_full': max_pages_full, 'ntl': ntl, 'nntl': nntl})
    else:
        return render(request, 'login.html')


#favorites to be implemented in the future
def view_my_favorites(request):
    return render(request, 'favorites.html')

def imprint(request):
    return render(request, 'imprint.html')

def rules(request):
    return render(request, 'rules.html')

def search(request):
    if not request.user.is_authenticated:
        return redirect_to_login('index', login_url='login_page')
    else:
        if request.method == 'GET':
            ref = request.GET.get('ref')
            keyword = request.GET.get('keyword')
            if ref == 'hashtag':
                pages = set(ContentItem.objects.filter(pk__in=ContentHashTag.objects.filter(hashtag_id__in=set(Hashtag.objects.filter(hashtag_text__icontains=keyword).values_list('pk', flat=True))).values_list('content_id', flat=True)))
            elif ref is not None:
                # search in referred board
                pages_hashtag = set(ContentItem.objects.filter(pk__in=ContentBoard.objects.filter(board_id__in=set(Board.objects.filter(name=ref).values_list('pk', flat=True))).values_list('content_id', flat=True)).filter(pk__in=ContentHashTag.objects.filter(hashtag_id__in=set(Hashtag.objects.filter(hashtag_text__icontains=keyword).values_list('pk', flat=True))).values_list('content_id', flat=True)))
                pages_title = set(ContentItem.objects.filter(title__icontains=keyword, pk__in=ContentBoard.objects.filter(board_id__in=set(Board.objects.filter(name=ref).values_list('pk', flat=True))).values_list('content_id', flat=True)))
                pages = pages_hashtag | pages_title
            else:
                pages_hashtag = set(ContentItem.objects.filter(pk__in=ContentHashTag.objects.filter(hashtag_id__in=set(Hashtag.objects.filter(hashtag_text__icontains=keyword).values_list('pk', flat=True))).values_list('content_id', flat=True)))
                pages_title = set(ContentItem.objects.filter(title__icontains=keyword))
                pages = pages_hashtag | pages_title

            for post in pages:
                tag_ids = list(set(ContentHashTag.objects.filter(content_id=post).values_list('hashtag_id', flat=True)))
                filtered_tags = list(set(Hashtag.objects.filter(pk__in=tag_ids).values_list('hashtag_text', flat=True)))
                post.tags = filtered_tags
            return render(request, 'search.html', {'pages': pages})
        return render(request, 'search.html')


def create_post(request):
    if not request.user.is_authenticated:
        return redirect_to_login('create_post', login_url='login_page')

    boards = Board.objects.all().values_list('name', flat=True)
    return render(request, 'createpost.html', {'boards': boards})


def login_page(request):
    if(request.method == 'POST'):
        name = request.POST['user']
       # if not User.objects.filter(username=name).exists():
        if not User.objects.filter(username__iexact=name).exists():
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

        if User.objects.filter(username__iexact= name).exists():
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

        board = request.POST.get('board', '<<post error>>')
        if board in set(Board.objects.all().values_list('name', flat=True)):
            board = Board.objects.get(name=board)
            content_board = ContentBoard(content_id=submitted_item, board_id=board)
            content_board.save()

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


def like_post(request):
    if request.method == 'GET':
        post_id = int(request.GET['post_id'])
        post = ContentItem.objects.get(id=post_id)
        new_like, created = Like.objects.get_or_create(user_id=request.user, content_id=post)
        if not created:
            Like.objects.filter(user_id=request.user, content_id=post).delete()
        likes = post.get_likes()
    return HttpResponse(likes)

@login_required
def downvote_comment(request):
    comment_id = None
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
    downvotes = 0
    if comment_id:
        comment = Comment.objects.get(id=int(comment_id))
        if comment:
            downvote, created = Downvote.objects.get_or_create(user_id=request.user, comment_id=comment)
            downvotes = comment.downvotes.count()
            data = json.dumps({
                'downvotes': downvotes })
        return HttpResponse(data, content_type='application/json')
    return HttpResponse("lalala")


@login_required
def upvote_comment(request):
    comment_id = None
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
    upvotes = 0
    if comment_id:
        comment = Comment.objects.get(id=int(comment_id))
        if comment:
            upvote, created = Upvote.objects.get_or_create(user_id=request.user, comment_id=comment)
            upvotes = comment.upvotes.count()
            data = json.dumps({
                'upvotes': upvotes})
        return HttpResponse(data, content_type='application/json')
    return HttpResponse("lalala")


def comment_on_item(request, content_id):
    if not request.user.is_authenticated:
        return redirect_to_login('comment', login_url='login_page')
    if request.method == 'POST':
        comment_text = request.POST['comment_text']
        if comment_text and not comment_text == "":
            author = request.user
            contentItem = ContentItem.objects.get(pk=content_id)
            new_comment = Comment(author=author, comment_text=comment_text, contentItem=contentItem)
            new_comment.save()
            data = json.dumps({
                'auth': author.username,
                'pic': author.profile.user_photo.url,
                'text': comment_text,
            })
        return HttpResponse(data, content_type='application/json')
        messages.warning(request, "Please write something.")
        # return HttpResponse("404")
    return HttpResponse("403")


def update_board_top_post(name):
    this = Board.objects.get(name=name)
    # get most liked post of the board
    top_post = ContentItem.objects.filter(pk__in=ContentBoard.objects.filter(board_id=Board.objects.filter(name=name)).values_list('content_id', flat=True)).annotate(count=Count('like')).order_by('-count')[:1]
    if len(top_post) > 0:
        top_post = top_post.get()
        this.top = top_post
        this.save()

def boards(request, board_name="def"):
    if not request.user.is_authenticated:
        return redirect_to_login('boards', login_url='login_page')
    else:
        top_boards = Board.objects.annotate(count=Count('contentboard')).order_by('-count')[:3]
        if board_name == "subscribed":
            boards = Board.objects.filter(pk__in=SubBoard.objects.filter(user=request.user).values_list('board_id', flat=True))
            return render(request, 'boards.html', {'all_boards': boards, 'top_boards': top_boards, 'sub': True})
        elif board_name == "def" or len(Board.objects.filter(name=board_name)) == 0:
            boards = Board.objects.all()
            return render(request, 'boards.html', {'all_boards': boards, 'top_boards': top_boards})
        else:
            subbed = len(SubBoard.objects.filter(user=request.user).filter(board_id=Board.objects.get(name=board_name)))
            update_board_top_post(board_name)
            board_content = ContentItem.objects.filter(pk__in=ContentBoard.objects.filter(board_id__in=Board.objects.filter(name=board_name.lower()).values_list('pk', flat=True)).values_list('content_id', flat=True))
            return render(request, 'boards.html', {'pages': board_content, 'board_name': board_name.lower(), 'top_boards': top_boards, 'subbed': subbed})


def create_board(request):
    if not request.user.is_authenticated:
        return redirect_to_login('createboard', login_url='login_page')
    else:
        return render(request, 'createboard.html')


def make_board(request):
    if not request.user.is_authenticated:
        return redirect_to_login('create_board', login_url='login_page')
    else:
        if request.method == 'POST' and request.user:
            submitted_name = request.POST.get('title', '<<post error>>').lower()
            if not any(char.isalpha() or char.isdigit() for char in submitted_name):
                messages.error(request, 'Name must contain at least one character or digit.')
                return redirect('create_board')
            submitted_description = request.POST.get('description', '<<post error>>')
            try:
                submitted_board = Board(name=submitted_name, description=submitted_description, admin=request.user, top=None)
                print(submitted_board.save())
                return redirect('boards')
            except:
                messages.error(request, 'Could not write to Database')
                return redirect('create_board')
        else:
            messages.error(request, 'Bad request.')
            return redirect('create_board')


def sub_board(request):
    if request.method == 'GET':
        board_name = request.GET['board_name']
        board = Board.objects.get(name=board_name)
        new_sub, created = SubBoard.objects.get_or_create(user=request.user, board_id=board)
        if not created:
            SubBoard.objects.filter(user=request.user, board_id=board).delete()
    return HttpResponse(created)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user profiles with full information to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class ContentItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows content items to be viewed or edited.
    """
    queryset = ContentItem.objects.all().order_by('-upload_date')
    serializer_class = serializers.ContentItemSerializer


class HashtagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hashtags to be viewed or edited.
    """
    queryset = Hashtag.objects.all()
    serializer_class = serializers.HashtagSerializer


class ContentHashtagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hashtags assigned to items to be viewed or edited.
    """
    queryset = ContentHashTag.objects.all()
    serializer_class = serializers.ContentHashtagSerializer


class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows likes to be viewed or edited.
    """
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class ContentItem(models.Model):
    upload_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='no title')
    description = models.CharField(max_length=400, default='no description')
    image = models.ImageField(upload_to='image_board/posts/', default='null')
    uploaded_by = models.ForeignKey(User, default='0')
    points = models.IntegerField(default=1000)
    points_weighted = models.IntegerField(default=1000)

    def __str__(self):
        return self.title

    def get_likes(self):
        no = self.like_set.all().count()
        if no is not None:
            return no
        else:
            return 0

    def get_comments(self):
        com = Comment.objects.filter(contentItem=self).annotate(num_up=Count('upvote')).order_by('-num_up', '-publication_date')
        return com


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    #email = models.EmailField()
    #first_name = models.CharField(max_length=20, blank=True)
    #last_name = models.CharField(max_length=20, blank=True)
    personal_info = models.TextField(blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    expertise = models.TextField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{5,15}$', message="Phone number must be entered in the format: '+123456'. Between 5 and 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)
    contact_skype = models.URLField(null=True, blank=True)
    contact_facebook = models.URLField(null=True, blank=True)
    contact_linkedin = models.URLField(null=True, blank=True)
    user_photo = models.ImageField(upload_to='../media/img', default='/static/img/anon.png')

    def __str__(self):
        return self.user.__str__()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Comment(models.Model):
    comment_text = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    contentItem = models.ForeignKey(ContentItem, on_delete= models.CASCADE, related_name="comments")

    def get_upvotes(self):
        no = self.upvote_set.all().count()
        if no is not None:
            return no
        else:
            return 0

class Upvote(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Hashtag(models.Model):
    hashtag_text = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.hashtag_text


class ContentHashTag(models.Model):
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)
    hashtag_id = models.ForeignKey(Hashtag, on_delete= models.CASCADE)


class Board(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150)
    admin = models.ForeignKey(User, on_delete= models.CASCADE)
    top = models.ForeignKey(ContentItem, on_delete= models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class ContentBoard(models.Model):
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)
    board_id = models.ForeignKey(Board, on_delete= models.CASCADE)


class SubBoard(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    board_id = models.ForeignKey(Board, on_delete= models.CASCADE)


class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)

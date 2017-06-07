from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ContentItem(models.Model):
    upload_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='no title')
    description = models.CharField(max_length=400, default='no description')
    image = models.ImageField(upload_to='image_board/posts/', default='null')
    uploaded_by = models.ForeignKey(User, default='0')

    def __str__(self):
        return self.title


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    personal_info = models.TextField(blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    expertise = models.TextField(blank=True)
    contact_phone = models.IntegerField(null=True, blank=True)
    contact_skype = models.URLField(null=True, blank=True)
    contact_facebook = models.URLField(null=True, blank=True)
    contact_linkedin = models.URLField(null=True, blank=True)
    user_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Comment(models.Model):
    title = models.CharField(max_length=100)
    comment_text = models.TextField()
    publication_date = models.DateField()
    user_id = models.ForeignKey(User)
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    hashtag_text = models.CharField(max_length=50)

    def __str__(self):
        return self.hashtag_text


class ContentHashTag(models.Model):
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)
    hashtag_id = models.ForeignKey(Hashtag, on_delete= models.CASCADE)



class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)

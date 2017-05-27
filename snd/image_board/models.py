from django.db import models
from django.core.urlresolvers import reverse


class UserPicture(models.Model):
    picture_id = models.PositiveIntegerField(primary_key=True)
    URL = models.URLField()
    user_photo = models.ImageField()

    def __str__(self):
        return self.picture_id


class User(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    personal_info = models.TextField()
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    expertise = models.TextField()
    contact_phone = models.IntegerField(null=True)
    contact_skype = models.URLField(null=True)
    contact_facebook = models.URLField(null=True)
    contact_linkedin = models.URLField(null=True)
    user_photo = models.ForeignKey(UserPicture, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class ContentItem(models.Model):
    content_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    URL = models.URLField(null=True)
    file_type = models.CharField(max_length=5)
    publication_date = models.DateField(null=True)
    author_id = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    comment_text = models.TextField()
    publication_date = models.DateField()
    user_id = models.ForeignKey(User)
    content_id = models.ForeignKey(ContentItem, limit_choices_to=ContentItem.content_id, on_delete= models.CASCADE)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    hashtag_id = models.PositiveIntegerField(primary_key=True)
    hashtag_text = models.CharField(max_length=50)

    def __str__(self):
        return self.hashtag_text


class ContentHashTag(models.Model):
    content_id = models.ForeignKey(ContentItem, limit_choices_to=ContentItem.content_id, on_delete= models.CASCADE)
    hashtag_id = models.ForeignKey(Hashtag, limit_choices_to=Hashtag.hashtag_id, on_delete= models.CASCADE)

    def __str__(self):
        return self.content_id


class Favorites(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content_id = models.ForeignKey(ContentItem, on_delete= models.CASCADE)

    def __str__(self):
        return self.content_id
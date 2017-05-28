from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import EmailValidator, validate_image_file_extension


class User(models.Model):
    email = models.EmailField(validators=[EmailValidator()])
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
    user_photo = models.ImageField(blank=True, validators=[validate_image_file_extension])

    def __str__(self):
        return self.first_name + " " + self.last_name


class ContentItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    URL = models.URLField(null=True)
    file_type = models.CharField(max_length=5)
    publication_date = models.DateField(null=True)
    author_id = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title


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
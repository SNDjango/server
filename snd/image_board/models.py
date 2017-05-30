from django.db import models
from django.contrib.auth.models import Permission, User

class ContentItem(models.Model):

    upload_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='no title')
    description = models.CharField(max_length=400, default='no description')
    image = models.ImageField(upload_to='image_board/posts/', default='null')
    uploaded_by = models.ForeignKey(User, default='0')

    def __str__(self):
        return self.title

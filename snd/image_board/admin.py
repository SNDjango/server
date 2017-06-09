from django.contrib import admin
from .models import Hashtag
from  .models import ContentItem
from  .models import Comment
from .models import ContentHashTag
from  .models import Favorite
from .models import Profile



# Register your models here.
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(ContentItem)
admin.site.register(Comment)
admin.site.register(ContentHashTag)
admin.site.register(Favorite)
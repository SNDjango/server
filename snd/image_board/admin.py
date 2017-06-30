from django.contrib import admin
from .models import Hashtag
from  .models import ContentItem
from  .models import Comment
from .models import ContentHashTag
from  .models import Favorite
from .models import Profile
from .models import CustomUser
from .models import Upvote
from .models import Downvote



# Register your models here.
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(ContentItem)
admin.site.register(Comment)
admin.site.register(ContentHashTag)
admin.site.register(Favorite)
admin.site.register(CustomUser)
admin.site.register(Upvote)
admin.site.register(Downvote)

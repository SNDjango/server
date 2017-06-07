from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from .models import Hashtag
from .models import ContentItem
from .models import Comment
from .models import ContentHashTag
from .models import Favorite


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# Register your models here.
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(ContentItem)
admin.site.register(Comment)
admin.site.register(ContentHashTag)
admin.site.register(Favorite)

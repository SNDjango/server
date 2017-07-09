from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'posts', views.ContentItemViewSet)
router.register(r'hashtags', views.HashtagViewSet)
router.register(r'content-hashtag', views.ContentHashtagViewSet)
router.register(r'likes', views.LikeViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_page, name='login_page'),
    url(r'^myprofile/$', views.IndexView.as_view(), name='profile'),
    url(r'^myprofile/edit$', views.update_profile, name='profile_edit'),
    url(r'^myprofile/picture/edit$', views.PicUpdate.as_view(), name='profile_pic_edit'),
    url(r'^profile/(?P<id>\d+)/$', views.profileview, name='profile_user'),
    url(r'^myposts$', views.view_my_posts, name='view_my_posts'),
    url(r'^myfavorites$', views.view_my_favorites, name='view_my_favorites'),
    url(r'^createpost$', views.create_post, name='create_post'),
    url(r'^myposts/delete/(?P<id>\d+)/$', views.delete_post, name='delete_post'),
    url(r'^imprint$', views.imprint, name='imprint'),
    url(r'^rules', views.rules, name='rules'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout_page, name='logout_page'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^changepassword$', views.change_password, name='changepw'),
    url(r'^search$', views.search, name='search'),
    url(r'^like-post/$', views.like_post, name='like_post'),
    url(r'^faq-page$', views.view_faq_page, name='faq_page'),
    url(r'^comment/([0-9]+)$', views.comment_on_item, name='comment_on_item'),
    url(r'^edit_comment/$', views.edit_comment, name='edit_comment'),
    url(r'^upvote_comment/$', views.upvote_comment, name='upvote_comment'),
    url(r'^boards/([0-9a-zA-Z ]+)$', views.boards, name='boards'),
    url(r'^boards$', views.boards, name='boards'),
    url(r'^createboard$', views.create_board, name='create_board'),
    url(r'^makeboard$', views.make_board, name='make_board'),
    url(r'^subscribe/$', views.sub_board, name='sub_board'),
    url(r'^restapi/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profile/delete$', views.delete_profile, name='delete_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

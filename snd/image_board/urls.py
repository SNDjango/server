from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_page, name='login_page'),
    url(r'^profile/$', views.IndexView.as_view(), name='profile'),
    url(r'^profile/edit$', views.update_profile, name='profile_edit'),
    url(r'^profile/picture/edit$', views.PicUpdate.as_view(), name='profile_pic_edit'),
    url(r'^myposts$', views.view_my_posts, name='view_my_posts'),
    url(r'^myfavorites$', views.view_my_favorites, name='view_my_favorites'),
    url(r'^createpost$', views.create_post, name='create_post'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout_page, name='logout_page'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^changepassword$', views.change_password, name='changepw'),
    url(r'^search$', views.search, name='search'),
    url(r'^like-post/$', views.like_post, name='like_post'),
<<<<<<< HEAD
    url(r'^faq-page$', views.view_faq_page, name='faq_page')

=======
    url(r'^comment/([0-9]+)$', views.comment_on_item, name='comment_on_item'),
>>>>>>> 96d478559b5bbff8fde8c103578c5c23ad43ca5e
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

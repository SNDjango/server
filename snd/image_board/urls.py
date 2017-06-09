from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_page, name='login_page'),
    url(r'^profile/edit$', views.UserUpdate.as_view(), name='profile_edit'),
    url(r'^profile/$', views.IndexView.as_view(), name='profile'),
    url(r'^myposts$', views.view_my_posts, name='view_my_posts'),
    url(r'^myfavorites$', views.view_my_favorites, name='view_my_favorites'),
    url(r'^createpost$', views.create_post, name='create_post'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout_page, name='logout_page'),
    url(r'^upload$', views.upload, name='upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_page, name='login_page'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^myposts$', views.view_my_posts, name='view_my_posts'),
    url(r'^myfavorites$', views.view_my_favorites, name='view_my_favorites'),
    url(r'^createpost$', views.create_post, name='create_post'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout_page, name='logout_page'),

]

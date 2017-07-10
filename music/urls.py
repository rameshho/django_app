from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /music/<pk>/
    # Detail view expects the primary key
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='Add-album'),

    #/music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='Update-album'),

    #/music/album/2/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='Delete-album'),
]
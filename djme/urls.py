from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'api.views.home', name='home'),
    url(r'^song_saver$', 'api.views.songs_saver', name='home'),
    url(r'^details$', 'api.views.details_saver', name='home'),
    # url(r'^song/(?P<foo>\w+)','api.views.song',name='adminSongPlaylist'),
    url(r'^song','api.views.song',name='adminSongPlaylist'),
)

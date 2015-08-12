from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static






urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include ('allauth.urls')),
    url(r'^$', 'videos.views.homepage', name='homepage'),
    url(r'^s/$', 'videos.views.search', name='search'),
    url(r'^content/', include('videos.urls')),
    url(r'^test/(?P<slug>[\w-]+)/$', 'accounts.views.add_to_list', name='add_to_list'),
    url(r'^favourite/$', 'accounts.views.user_content', name='favourite'),
    url(r'^learned/$', 'accounts.views.user_content', name='learned'),
    url(r'^later/$', 'accounts.views.user_content', name='later'),
    url(r'^added-by-me/$', 'accounts.views.user_content', name='added-by-me'),
    url(r'^user-detail/$', 'accounts.views.user_detail', name='user_detail'),
    url(r'^(?P<id>\d+)/$', 'accounts.views.single_user', name='single-user'),
    url(r'^events/$', 'events.views.event_view', name='events'),
    url(r'^events/my$', 'events.views.user_event_view', name='my_events'),
    url(r'^events/attending$', 'events.views.attending_view', name='attending'),
    url(r'events/category/(?P<slug_cat>[\w-]+)/$', 'events.views.category_event', name='category-event'),
    url(r'events/(?P<slug>[\w-]+)/$', 'events.views.event_detail', name='event-detail'),
    url(r'^add-event/$', 'events.views.add_event', name='add_event'),
    url(r'^edit-event/(?P<id>\d+)/$', 'events.views.edit_event', name='edit-event'),
    url(r'^users/$', 'accounts.views.all_users', name='users'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
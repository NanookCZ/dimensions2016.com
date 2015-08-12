from django.conf.urls import include, url



urlpatterns = [
    url(r'category/(?P<slug_cat>[\w-]+)/$', 'videos.views.category_content', name='category'),
    url(r'category/(?P<slug_cat>[\w-]+)/(?P<slug_con>[\w-]+)/$', 'videos.views.content_list', name='content-list'),
    url(r'content-type/(?P<slug_con>[\w-]+)/$', 'videos.views.content_type_content', name='content-type'),
    url(r'(?P<slug_con>[\w-]+)/$', 'videos.views.content_detail', name='content-detail'),
    
    ]
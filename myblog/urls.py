from django.conf.urls import include, url
from django.contrib import admin
import article.views as article_views
import some_api.views as api_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',article_views.home),
    url(r'^(?P<id>\d+)/$', 'article.views.per_page', name='per_page'),
    url(r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/images'}),
    url(r'book','some_api.views.get_user_collection', name='get_user_collection'),
]

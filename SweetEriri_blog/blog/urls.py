from django.conf.urls import url
from . import views
from django.conf import settings
from django.views import static
from django.conf.urls import handler404, handler500, handler403
from .views import page_not_found, page_error, resources_not_available

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]

# 404 页面找不到
handler404 = page_not_found
# 500 服务器出错
handler500 = page_error
# 资源不可用
handler403 = resources_not_available

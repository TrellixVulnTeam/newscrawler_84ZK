from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # users
    url(r'api/users/top/submitters/$', views.TopSubmitters.as_view(), name='topSubmitters'),
    url(r'api/users/(?P<username>[^/]+)/posts/$', views.PostsUser.as_view(), name='postsUser'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

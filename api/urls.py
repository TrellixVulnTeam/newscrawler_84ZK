from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    #submissions
    url(r'api/submissions/(?P<id>[^/]+)/$', views.SubmissionView.as_view(), name='submission'),
    # users
    url(r'api/users/(?P<id>[^/]+)/$', views.UserView.as_view(), name='users'),
    url(r'api/users/(?P<id>[^/]+)/posts/$', views.PostsUser.as_view(), name='postsUser'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # submissions
    url(r'api/submissions/top/points/(?P<type_submission>[^/]+)/', views.TopPointsSubmissions.as_view(), name='topPointsSubmissions'),
    url(r'api/submissions/top/discussed/(?P<type_submission>[^/]+)/$', views.TopCommentsSubmissions.as_view(), name='topCommentsSubmissions'),
    # users
    url(r'api/users/top/submitters/$', views.TopSubmitters.as_view(), name='topSubmitters'),
    url(r'api/users/(?P<username>[^/]+)/posts/$', views.PostsUser.as_view(), name='postsUser'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

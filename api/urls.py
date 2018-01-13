from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # top 10 submissions by points
    url(r'api/submissions/top/points/$', views.TopPointsSubmissions.as_view(), name='topPointsSubmissions'),
    url(r'api/submissions/top/points/discussions/$', views.TopPointsDiscussions.as_view(), name='topPointsDiscussions'),
    url(r'api/submissions/top/points/articles/$', views.TopPointsArticles.as_view(), name='topPointsArticles'),
    # top 10 discussed submissions
    url(r'api/submissions/top/discussed/$', views.TopCommentsSubmissions.as_view(), name='topCommentsSubmissions'),
    url(r'api/submissions/top/discussed/discussions/$', views.TopCommentsDiscussions.as_view(), name='topCommentsDiscussions'),
    url(r'api/submissions/top/discussed/articles/$', views.TopCommentsArticles.as_view(), name='topCommentsArticles'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

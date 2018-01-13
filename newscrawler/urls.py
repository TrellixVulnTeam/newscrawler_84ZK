from api.views import *
from django.conf.urls import include, url
from rest_framework import routers


# this is DRF router for REST API viewsets
router = routers.DefaultRouter()
router.register(r'submissions/top/points/any', TopPointSubmissions, r"Pointsubmission")
router.register(r'submissions/top/points/discussions', TopPointDiscussions, r"PointDiscussions")
router.register(r'submissions/top/points/articles', TopPointArticles, r"PointArticles")
router.register(r'submissions/top/discussed/any', TopDiscussedSubmissions, r"DiscussedSubmission")
router.register(r'submissions/top/discussed/discussions', TopDiscussedDiscussions, r"DiscussedDiscussions")
router.register(r'submissions/top/discussed/articles', TopDiscussedArticles, r"DiscussedArticles")

urlpatterns = [
    # apiview
    url(r'^', include('api.urls')),
    # viewsets
    url(r'^api/', include(router.urls)),
]

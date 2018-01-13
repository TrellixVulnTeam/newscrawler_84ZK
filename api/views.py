from api.models import *
from rest_framework.response import Response
from rest_framework.views import APIView


#####################################
#########   Submissions    ##########
#####################################
class TopPointsSubmissions(APIView):

    def get(self, request, format=None):
        # Top 10 submissions ordered by punctuation (desc)
        submissions = Submission.objects.order_by('-punctuation')[:10].to_json()
        return Response(submissions)


class TopPointsDiscussions(APIView):

    def get(self, request, format=None):
        # Top 10 submissions that are discussions ordered by punctuation (desc)
        submissions = Submission.objects(is_discussion=True).order_by('-punctuation')[:10].to_json()
        return Response(submissions)


class TopPointsArticles(APIView):

    def get(self, request, format=None):
        # Top 10 submissions that are articles ordered by punctuation (desc)
        submissions = Submission.objects(is_discussion=False).order_by('-punctuation')[:10].to_json()
        return Response(submissions)


class TopCommentsSubmissions(APIView):

    def get(self, request, format=None):
        # Top 10 submissions ordered by number of comments (desc)
        submissions = Submission.objects.order_by('-number_comments')[:10].to_json()
        return Response(submissions)


class TopCommentsDiscussions(APIView):

    def get(self, request, format=None):
        # Top 10 submissions that are discussions ordered by number of comments (desc)
        submissions = Submission.objects(is_discussion=True).order_by('-number_comments')[:10].to_json()
        return Response(submissions)


class TopCommentsArticles(APIView):

    def get(self, request, format=None):
        # Top 10 submissions that are articles ordered by number of comments (desc)
        submissions = Submission.objects(is_discussion=False).order_by('-number_comments')[:10].to_json()
        return Response(submissions)

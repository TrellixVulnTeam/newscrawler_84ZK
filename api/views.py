import json
from api.serializers import *
from bson import ObjectId
from rest_framework import status
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


# To make ObjectID serializable
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


#####################################
#########   Submissions    ##########
#####################################
class SubmissionView(APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        # Check format id
        try:
            ObjectId(id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        submission = json.loads(Submission.objects(pk=id).to_json())  # Get the submission and parse to json
        # Check if id exists
        if len(submission) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(submission[0])  # Only the first item is the submission


class TopPointSubmissions(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects.order_by('-punctuation')[:10]


class TopPointDiscussions(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects(is_discussion=True).order_by('-punctuation')[:10]


class TopPointArticles(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects(is_discussion=False).order_by('-punctuation')


class TopDiscussedSubmissions(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects.order_by('-number_comments')[:10]


class TopDiscussedDiscussions(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects(is_discussion=True).order_by('-number_comments')[:10]


class TopDiscussedArticles(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects(is_discussion=False).order_by('-number_comments')[:10]


#####################################
#########      Users       ##########
#####################################
class UserView(APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        # Check format id
        try:
            ObjectId(id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = json.loads(User.objects(pk=id).to_json())  # Get the user and parse to json
        # Check if id exists
        if len(user) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(user[0])  # Only the first item is the user


class PostsUser(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        # Check format id
        try:
            ObjectId(id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = User.objects(pk=id)
        # Check if id exists
        if len(user) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Get submissions of the user, user[0] because id is unique
        user_submissions = []
        for submission in user[0].submissions:
            user_submissions.append(json.loads(submission.to_json()))
        return Response(user_submissions)


class TopSubmitters(viewsets.ModelViewSet):
    serializer_class = TopUserSerializer

    def get_queryset(self):
        # Count length of submissions array and sort by this length
        pipeline = [
            {
                "$project": {
                    "id": "$_id",
                    "username": "$username",
                    "numberOfSubmissions": {"$size": "$submissions"}
                }
            },
            {"$sort": {"numberOfSubmissions": -1}}
        ]
        # Top 10 submitters only
        top_submitters = []
        i = 0
        for user in User.objects.aggregate(*pipeline):
            if i < 10:
                top_submitters.append(json.loads(JSONEncoder().encode(user)))
            i = i + 1
        return top_submitters



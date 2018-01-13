import json
from api.models import User, Submission
from bson import ObjectId
from rest_framework import status
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
class TopPointsSubmissions(APIView):

    def get(self, request, *args, **kwargs):
        type_submission = kwargs.get('type_submission')
        if type_submission == 'any':
            # Top 10 submissions ordered by punctuation (desc)
            submissions = Submission.objects.order_by('-punctuation')[:10].to_json()
        elif type_submission == 'discussions':
            # Top 10 submissions that are discussions ordered by punctuation (desc)
            submissions = Submission.objects(is_discussion=True).order_by('-punctuation')[:10].to_json()
        elif type_submission == 'articles':
            # Top 10 submissions that are articles ordered by punctuation (desc)
            submissions = Submission.objects(is_discussion=False).order_by('-punctuation')[:10].to_json()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(json.loads(submissions))


class TopCommentsSubmissions(APIView):

    def get(self, request, *args, **kwargs):
        type_submission = kwargs.get('type_submission')
        if type_submission == 'any':
            # Top 10 submissions ordered by number of comments (desc)
            submissions = Submission.objects.order_by('-number_comments')[:10].to_json()
        elif type_submission == 'discussions':
            # Top 10 submissions that are discussions ordered by number of comments (desc)
            submissions = Submission.objects(is_discussion=True).order_by('-number_comments')[:10].to_json()
        elif type_submission == 'articles':
            # Top 10 submissions that are articles ordered by number of comments (desc)
            submissions = Submission.objects(is_discussion=False).order_by('-number_comments')[:10].to_json()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(json.loads(submissions))


#####################################
#########      Users       ##########
#####################################
class TopSubmitters(APIView):

    def get(self, request, *args, **kwargs):
        # Count length of submissions array and sort by this length
        pipeline = [
            {
                "$project": {
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

        return Response(top_submitters)


class PostsUser(APIView):

    def get(self, requet, *args, **kwargs):
        username = kwargs.get('username', None)
        user = User.objects(username=username)
        if len(user) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # Get submissions of the user, user[0] because username is unique
        user_submissions = []
        for submission in user[0].submissions:
            user_submissions.append(json.loads(Submission.objects.get(id=submission).to_json()))
        return Response(user_submissions)


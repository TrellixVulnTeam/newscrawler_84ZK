from api.models import *
from rest_framework_mongoengine import serializers as mongoserialiers
from rest_framework import serializers


class SubmissionSerializer(mongoserialiers.DocumentSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class UserSerializer(mongoserialiers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TopUserSerializer(mongoserialiers.DocumentSerializer):
    numberOfSubmissions = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id', 'username', 'numberOfSubmissions')
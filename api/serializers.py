from api.models import *
from rest_framework_mongoengine import serializers


class SubmissionSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Submission
        fields = '__all__'


class UserSerialier(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'

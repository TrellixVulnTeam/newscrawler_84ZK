from mongoengine import *


class User(Document):
    username = StringField()
    submissions = ListField()

    meta = {
        'collection': 'users'  # Collection name in MongoDB
    }


class Submission(Document):
    punctuation = IntField()
    number_comments = IntField()
    url = StringField()
    is_discussion = BooleanField()
    title = StringField()
    creation_date = StringField()

    meta = {
        'collection': 'submissions'  # Collection name in MongoDB
    }

import json
from api.models import *
from django.test import TestCase
from rest_framework import status


class ApiTestCase(TestCase):

    # Define a test database
    @classmethod
    def setUpClass(cls):
        super(ApiTestCase, cls).setUpClass()
        s1 = Submission(10, 1, 'https://www.google.com', False, 'Google page', '13/01/2018')
        s1.save()
        s2 = Submission(1, 10, 'https://www.reddit.com/r/Python/subreddit', True, 'Reddit 1', '12/01/2018')
        s2.save()
        s3 = Submission(100, 11, 'https://www.maps.google.com', False, 'Google maps page', '11/01/2018')
        s3.save()
        s4 = Submission(90, 90, 'https://www.reddit.com/r/Python/subreddit', True, 'Reddit 2', '12/01/2018')
        s4.save()
        s5 = Submission(80, 100, 'https://www.maps.google.com', False, 'Google maps page', '11/01/2018')
        s5.save()
        s6 = Submission(6, 20, 'https://www.reddit.com/r/Python/subreddit', True, 'Reddit 3', '12/01/2018')
        s6.save()
        s7 = Submission(0, 30, 'https://www.maps.google.com', False, 'Google maps page', '11/01/2018')
        s7.save()
        s8 = Submission(0, 80, 'https://www.reddit.com/r/Python/subreddit', True, 'Reddit 4', '12/01/2018')
        s8.save()
        s9 = Submission(17, 9, 'https://www.maps.google.com', False, 'Google maps page', '11/01/2018')
        s9.save()
        s10 = Submission(28, 25, 'https://www.reddit.com/r/Python/subreddit', True, 'Reddit 5', '12/01/2018')
        s10.save()
        submission_u1 = [s1.id, s2.id]
        u1 = User(username="user1", submissions=submission_u1)
        u1.save()
        submission_u2 = [s3.id, s4.id, s5.id, s6.id, s7.id, s8.id, s9.id, s10.id]
        u2 = User(username="user2", submissions=submission_u2)
        u2.save()

    def test_get_submissions(self):
        """
        Ensure connection with Submission collection
        """
        submissions = Submission.objects
        self.assertEqual(10, submissions[0].punctuation)
        self.assertEqual(True, submissions[1].is_discussion)
        self.assertEqual('https://www.maps.google.com', submissions[2].url)

    def test_get_users(self):
        """
        Ensure connection with User collection
        """
        users = User.objects
        self.assertEqual('user1', users[0].username)
        self.assertEqual('user2', users[1].username)

    def test_api_top_points(self):
        """
        Ensure API call of top points.
        """
        url = 'http://127.0.0.1:8000/api/submissions/top/points/any/'
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['punctuation'], 100)
        self.assertEqual(json_response[1]['punctuation'], 90)
        self.assertEqual(json_response[2]['punctuation'], 80)
        self.assertEqual(json_response[3]['punctuation'], 28)
        self.assertEqual(json_response[4]['punctuation'], 17)
        self.assertEqual(json_response[5]['punctuation'], 10)
        self.assertEqual(json_response[6]['punctuation'], 6)
        self.assertEqual(json_response[7]['punctuation'], 1)
        self.assertEqual(json_response[8]['punctuation'], 0)
        self.assertEqual(json_response[9]['punctuation'], 0)

    def test_api_top_points_discussions(self):
        """
        Ensure API call of top points (only for discussions).
        """
        url = 'http://127.0.0.1:8000/api/submissions/top/points/discussions/'
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['punctuation'], 90)
        self.assertEqual(json_response[1]['punctuation'], 28)
        self.assertEqual(json_response[2]['punctuation'], 6)
        self.assertEqual(json_response[3]['punctuation'], 1)
        self.assertEqual(json_response[4]['punctuation'], 0)

    def test_api_top_points_articles(self):
        """
        Ensure API call of top points (only for articles).
        """
        url = 'http://127.0.0.1:8000/api/submissions/top/points/articles/'
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['punctuation'], 100)
        self.assertEqual(json_response[1]['punctuation'], 80)
        self.assertEqual(json_response[2]['punctuation'], 17)
        self.assertEqual(json_response[3]['punctuation'], 10)
        self.assertEqual(json_response[4]['punctuation'], 0)

    def test_api_top_comments(self):
        """
        Ensure API call of top discussed.
        """
        url = 'http://127.0.0.1:8000/api/submissions/top/discussed/any/'
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['number_comments'], 100)
        self.assertEqual(json_response[1]['number_comments'], 90)
        self.assertEqual(json_response[2]['number_comments'], 80)
        self.assertEqual(json_response[3]['number_comments'], 30)
        self.assertEqual(json_response[4]['number_comments'], 25)
        self.assertEqual(json_response[5]['number_comments'], 20)
        self.assertEqual(json_response[6]['number_comments'], 11)
        self.assertEqual(json_response[7]['number_comments'], 10)
        self.assertEqual(json_response[8]['number_comments'], 9)
        self.assertEqual(json_response[9]['number_comments'], 1)

    def test_api_top_comments_discussions(self):
        """
        Ensure API call of top discussed (only for discussions).
        """
        url = 'http://127.0.0.1:8000/api/submissions/top/discussed/discussions/'
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['number_comments'], 90)
        self.assertEqual(json_response[1]['number_comments'], 80)
        self.assertEqual(json_response[2]['number_comments'], 25)
        self.assertEqual(json_response[3]['number_comments'], 20)
        self.assertEqual(json_response[4]['number_comments'], 10)

    def test_api_top_comments_articles(self):
        """
        Ensure API call of top discussed (only for articles).
        """
        url = 'http://127.0.0.1:8000/api/submissions/top/discussed/articles/'
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['number_comments'], 100)
        self.assertEqual(json_response[1]['number_comments'], 30)
        self.assertEqual(json_response[2]['number_comments'], 11)
        self.assertEqual(json_response[3]['number_comments'], 9)
        self.assertEqual(json_response[4]['number_comments'], 1)

    def test_api_top_submitters(self):
        """
        Ensure API call of top submitters.
        """
        url = 'http://127.0.0.1:8000/api/users/top/submitters/'
        response = self.client.get(url, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['numberOfSubmissions'], 8)
        self.assertEqual(json_response[1]['numberOfSubmissions'], 2)

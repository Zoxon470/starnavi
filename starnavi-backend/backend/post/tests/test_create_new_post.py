from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

class PostEndpointTestCase(TestCase):
    def setUpTestData(cls):
        cls.create_post_url = reverse('post:create')

    def setUp(self):
        self.post_id = '123'

    def test_create_new_post(self):
        res = self.client.post(self.create_post_url, self.post_id)

        self.assertEqual(res, Response())

    def test_create_new_post_error(self):
        res = self.client.post(self.create_post_url, self.post_id)

        self.assertEqual(res.message, 'User has already liked this post.')

    def test_create_new_post_other_test(self):
        res = self.client.post(self.create_post_url, self.post_id)

        self.assertEqual(res.message, 'User has already liked this post.')
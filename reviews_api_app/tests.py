from .models import Reviews
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
# Create your tests here.


class reviwTests(TestCase):

    @classmethod
    #must be setUpTestData
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='liyan', password='123456')
        
        test_user.save()

        test_post = Reviews.objects.create(
            item =  'coffe machine',
            review = 'its amazing , I make many delicious types of coffee',
            purchaser = test_user,
        )

        test_post.save()

    def test_content(self):

        post = Reviews.objects.get(id=1)
        actual_item = str(post.item)
        actual_review = str(post.review)
        actual_purchaser = str(post.purchaser)

        self.assertEqual(actual_item, 'coffe machine')
        self.assertEqual(actual_review, 'its amazing , I make many delicious types of coffee')
        self.assertEqual(actual_purchaser, 'liyan')

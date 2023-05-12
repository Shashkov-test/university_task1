from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Article, Category

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test 
        Category.objects.create(category='Innovations', 
                                slug='innovations')

    def test_get_absolute_url(self):
        category=Category.objects.get(id=1)

        self.assertEquals(category.get_absolute_url(),
        '/articles/category/innovations')




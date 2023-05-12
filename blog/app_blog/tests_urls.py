# app_blog/tests.py
from django.urls import reverse, resolve
from django.test import TestCase
from app_blog.views import HomePageView
from app_blog.models import Article



class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, 
                         HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_news_detail_status_code(self):
        article = Article.objects.create(title='Test Article', slug='test-article')
        url = reverse('news-detail', args=(article.pub_date.year, article.pub_date.month, article.pub_date.day, article.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)




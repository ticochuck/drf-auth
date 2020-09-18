from django.test import TestCase
from django.contrib.auth.models import User

from .models import Article


class ArticleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', 
            password='testing123456'
        )

        testuser1.save()

        test_article = Article.objects.create(
            author=testuser1, 
            title='Bad Air', 
            body='Air quality is bad'
        )
        
        test_article.save()


    def test_article_content(self):
        article = Article.objects.get(id=1)
        actual_author = f'{article.author}'
        actual_title = f'{article.title}'
        actual_body = f'{article.body}'
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Bad air')
        self.assertEqual(actual_body, 'Air quality is bad')
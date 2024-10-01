""" Tests for blog.categories.models """

from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.articles.models import Article
from blog.categories.models import Category


# Create your tests here.
User = get_user_model()


class CategoryTests(TestCase):
    """Category model tests"""

    def setUp(self) -> None:
        """Setup data"""

        # Article owner
        user = User(username="article_owner", email="user@example.com")
        user.save()
        self.user = user

        # Category
        category = Category(name="Test", description="Test Category")
        category.save()
        self.category = category

        # Article
        article = Article(
            category=category,
            user=user,
            title="Test",
            headline="Test headline",
            content="Test content...",
        )
        article.save()
        self.article = article

        return super().setUp()

    def test_article_count(self):
        """Test for category.article_count"""

        self.assertEqual(self.category.article_count, 1)

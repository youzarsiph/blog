""" Tests for blog.tags.models """

from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.articles.models import Article
from blog.categories.models import Category
from blog.tags.models import Tag


# Create your tests here.
User = get_user_model()


class TagTests(TestCase):
    """Tag model tests"""

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
            user=user,
            category=category,
            title="Test",
            headline="Test headline",
            content="Test content...",
        )
        article.save()
        self.article = article

        # Tag
        tag = Tag(name="Test", description="Test tag", color="#fff")
        tag.save()
        self.tag = tag

        return super().setUp()

    def test_article_count(self):
        """Test for article.article_count"""

        # Initial count
        self.assertEqual(self.tag.article_count, 0)

        # Count after adding a article
        self.article.tags.add(self.tag)

        self.assertEqual(self.tag.article_count, 1)

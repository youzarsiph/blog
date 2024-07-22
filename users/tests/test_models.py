""" Tests for blog.users.models """

from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.articles.models import Article


# Create your tests here.
User = get_user_model()


class UserTests(TestCase):
    """User model tests"""

    def setUp(self) -> None:
        """Setup data"""

        # Article owner
        user = User(username="article_owner", email="user@example.com")
        user.save()
        self.user = user

        return super().setUp()

    def test_article_count(self):
        """Test for user.article_count"""

        # Initial count
        self.assertEqual(self.user.article_count, 0)

        # Count after adding a article
        article = Article(
            user=self.user,
            title="Test",
            headline="Test headline",
            content="Test content...",
        )
        article.save()

        self.assertEqual(self.user.article_count, 1)

    def test_follower_count(self):
        """Test for user.follower_count"""

        # Initial count
        self.assertEqual(self.user.follower_count, 0)

        # Count after adding a follower
        self.user.followers.add(self.user)

        self.assertEqual(self.user.follower_count, 1)

""" Tests for blog.comments.models """

from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.articles.models import Article
from blog.categories.models import Category
from blog.comments.models import Comment


# Create your tests here.
User = get_user_model()


class CommentTests(TestCase):
    """Comment model tests"""

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

        comment = Comment(
            user=user,
            article=article,
            content="Some comment...",
        )
        comment.save()
        self.comment = comment

        return super().setUp()

    def test_comment_count(self):
        """Test for article.comment_count"""

        # Initial count
        self.assertEqual(self.comment.reply_count, 0)

        # Count after adding a comment
        comment = Comment(
            user=self.user,
            article=self.article,
            content="Some content...",
        )
        comment.save()
        self.comment.replies.add(comment)

        self.assertEqual(self.comment.reply_count, 1)

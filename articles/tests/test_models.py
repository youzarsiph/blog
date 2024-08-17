""" Tests for blog.articles.models """

from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.articles.models import Article
from blog.categories.models import Category
from blog.comments.models import Comment
from blog.reactions.models import Reaction
from blog.tags.models import Tag


# Create your tests here.
User = get_user_model()


class ArticleTests(TestCase):
    """Article model tests"""

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

        return super().setUp()

    def test_comment_count(self):
        """Test for article.comment_count"""

        # Initial count
        self.assertEqual(self.article.comment_count, 0)

        # Count after adding a comment
        comment = Comment(
            user=self.user,
            article=self.article,
            content="Some content...",
        )
        comment.save()

        self.assertEqual(self.article.comment_count, 1)

    def test_reaction_count(self):
        """Test for article.reaction_count"""

        # Initial count
        self.assertEqual(self.article.reaction_count, 0)

        # Count after adding a reaction
        reaction = Reaction(user=self.user, article=self.article)
        reaction.save()

        self.assertEqual(self.article.reaction_count, 1)

    def test_tag_count(self):
        """Test for article.tag_count"""

        # Initial count
        self.assertEqual(self.article.tag_count, 0)

        # Count after adding a tag
        tag = Tag(name="Test", description="Test tag", color="#fff")
        tag.save()

        self.article.tags.add(tag)
        self.assertEqual(self.article.tag_count, 1)

    def test_stars(self):
        """Test for article.stars"""

        # Initial count
        self.assertEqual(self.article.stars, 0)

        # Count after adding a reaction
        self.article.stargazers.add(self.user)
        self.assertEqual(self.article.stars, 1)

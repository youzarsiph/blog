""" Data Models for blog.articles """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Article(models.Model):
    """Articles"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles",
        help_text="Article Owner",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Article title",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Article Photo",
        upload_to="blog/images/articles/",
    )
    content = models.TextField(
        db_index=True,
        help_text="Article content",
    )
    is_pinned = models.BooleanField(
        default=False,
        help_text="Designates if the Article is pinned",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        related_name="articles",
        help_text="Article tags",
    )
    reactions = models.ManyToManyField(
        User,
        related_name="reactions",
        through="reactions.Reaction",
        help_text="Article reactions",
    )
    comments = models.ManyToManyField(
        User,
        related_name="comments",
        through="comments.Comment",
        help_text="Article comments",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date published",
    )

    @property
    def comment_count(self) -> int:
        """Number of comments of an article"""

        return self.comments.count()

    @property
    def reaction_count(self) -> int:
        """Number of reactions of an article"""

        return self.reactions.count()

    @property
    def tag_count(self) -> int:
        """Number of tags of an article"""

        return self.tags.count()

    def __str__(self) -> str:
        return self.title

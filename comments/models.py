""" Data Models for blog.comments """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Comment(models.Model):
    """Comments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Comment Owner",
    )
    article = models.ForeignKey(
        "articles.Article",
        on_delete=models.CASCADE,
        help_text="Commented Article",
    )
    content = models.TextField(
        db_index=True,
        help_text="Content",
    )
    extras = models.JSONField(
        null=True,
        blank=True,
        help_text="Comment extra data like summary etc...",
    )
    replies = models.ManyToManyField(
        "self",
        symmetrical=False,
        help_text="Comment Replies",
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
    def reply_count(self) -> int:
        """Number of replies to this comment"""

        return self.replies.count()

    def __str__(self) -> str:
        return f"Comment by {self.user} on {self.article}: {self.content[:20]}..."

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
    text = models.TextField(
        db_index=True,
        help_text="Content",
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

    def __str__(self) -> str:
        return super().__str__()

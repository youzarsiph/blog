""" Data Models for blog.followers """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Follower(models.Model):
    """Followers"""

    from_user = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE,
        help_text="Follower",
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Followed",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date followed",
    )

    class Meta:
        """Meta data"""

        indexes = [models.Index(fields=["from_user", "to_user"])]
        constraints = [
            models.UniqueConstraint(
                fields=["from_user", "to_user"],
                name="unique_follower",
            )
        ]

    def __str__(self) -> str:
        return super().__str__()

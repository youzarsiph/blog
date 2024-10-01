""" Data models for blog.users """

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Blog Users"""

    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="User photo",
        upload_to="blog/images/users/",
    )
    cover = models.ImageField(
        null=True,
        blank=True,
        help_text="User cover",
        upload_to="blog/images/covers/",
    )
    bio = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="User bio",
    )
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        through="followers.Follower",
        help_text="User followers",
    )

    @property
    def article_count(self) -> int:
        """Number of articles of a user"""

        return self.articles.count()

    @property
    def follower_count(self) -> int:
        """Number of followers of a user"""

        return self.followers.count()

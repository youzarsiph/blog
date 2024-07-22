""" Data Models for blog.reports """

from django.db import models
from django.contrib.auth import get_user_model


REPORT_REASONS = (
    (0, "Rude or vulgar"),
    (1, "Harassment or hate speech"),
    (2, "Spam"),
    (3, "Copy right issue"),
    (4, "Inappropriate"),
    (5, "Other"),
)


# Create your models here.
User = get_user_model()


class Report(models.Model):
    """Abuse Reports"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Reporter",
    )
    article = models.ForeignKey(
        "articles.Article",
        on_delete=models.CASCADE,
        help_text="Reported Article",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the abuse report is correct",
    )
    message = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Message that will help us understand and handle the situation",
    )
    reason = models.PositiveSmallIntegerField(
        default=0,
        db_index=True,
        help_text="Report reason",
        choices=REPORT_REASONS,
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
        return f"{self.user} --{REPORT_REASONS[self.reason][1]}-> {self.article}"

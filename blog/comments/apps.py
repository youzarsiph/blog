""" AppConf for blog.comments """

from django.apps import AppConfig


# Create your AppConf here.
class CommentsConfig(AppConfig):
    """App Configuration for blog.comments"""

    name = "blog.comments"
    default_auto_field = "django.db.models.BigAutoField"

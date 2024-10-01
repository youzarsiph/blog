""" AppConf for blog.followers """

from django.apps import AppConfig


# Create your AppConf here.
class FollowersConfig(AppConfig):
    """App Configuration for blog.followers"""

    name = "blog.followers"
    default_auto_field = "django.db.models.BigAutoField"

""" AppConf for blog.tags """

from django.apps import AppConfig


# Create your AppConf here.
class TagsConfig(AppConfig):
    """App Configuration for blog.tags"""

    name = "blog.tags"
    default_auto_field = "django.db.models.BigAutoField"

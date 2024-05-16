""" AppConf for blog """

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """App configuration for blog"""

    name = "blog"
    default_auto_field = "django.db.models.BigAutoField"

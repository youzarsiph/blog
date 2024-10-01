""" AppConf for blog.articles """

from django.apps import AppConfig


# Create your AppConf here.
class ArticlesConfig(AppConfig):
    """App Configuration for blog.articles"""

    name = "blog.articles"
    default_auto_field = "django.db.models.BigAutoField"

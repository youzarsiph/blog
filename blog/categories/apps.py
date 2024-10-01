""" AppConf for blog.categories """

from django.apps import AppConfig


# Create your AppConf here.
class CategoriesConfig(AppConfig):
    """App Configuration for blog.categories"""

    name = "blog.categories"
    default_auto_field = "django.db.models.BigAutoField"

""" AppConf for blog.users """

from django.apps import AppConfig


# Create your AppConf here.
class UsersConfig(AppConfig):
    """App configuration for blog.users"""

    name = "blog.users"
    default_auto_field = "django.db.models.BigAutoField"

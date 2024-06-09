""" Serializers for blog.users """

from rest_framework.serializers import ModelSerializer
from blog.users.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta data"""

        model = User
        read_only_fields = ["date_joined", "last_login"]
        fields = [
            "id",
            "url",
            "photo",
            "cover",
            "username",
            "first_name",
            "last_name",
            "bio",
            "article_count",
            "follower_count",
            "date_joined",
            "last_login",
        ]

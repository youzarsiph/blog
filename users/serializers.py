""" Serializers for blog.users """

from rest_framework.serializers import ModelSerializer
from blog.users.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = [
            "id",
            "url",
            "photo",
            "username",
            "first_name",
            "last_name",
            "article_count",
            "follower_count",
        ]


class UserRetrieveSerializer(UserSerializer):
    """User Serializer for retrieve action"""

    class Meta(UserSerializer.Meta):
        """Meta data"""

        depth = 1
        read_only_fields = ["date_joined", "last_login", "articles"]
        fields = UserSerializer.Meta.fields + [
            "articles",
            "cover",
            "email",
            "bio",
            "date_joined",
            "last_login",
        ]

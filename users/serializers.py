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
            "username",
            "first_name",
            "last_name",
            "bio",
            "date_joined",
            "last_login",
            "created_at",
            "updated_at",
        ]

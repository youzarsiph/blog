""" Serializers for blog.followers """

from rest_framework.serializers import ModelSerializer
from blog.followers.models import Follower


# Create your serializers here.
class FollowerSerializer(ModelSerializer):
    """Follower Serializer"""

    class Meta:
        """Meta data"""

        model = Follower
        read_only_fields = ["from_user", "to_user"]
        fields = [
            "id",
            "url",
            "from_user",
            "to_user",
            "created_at",
            "updated_at",
        ]

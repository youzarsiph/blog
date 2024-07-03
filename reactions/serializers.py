""" Serializers for blog.reactions """

from rest_framework.serializers import ModelSerializer
from blog.reactions.models import Reaction
from blog.users.serializers import UserSerializer


# Create your serializers here.
class ReactionSerializer(ModelSerializer):
    """Reaction Serializer"""

    user = UserSerializer(read_only=True)

    class Meta:
        """Meta data"""

        model = Reaction
        read_only_fields = ["user", "article"]
        fields = [
            "id",
            "url",
            "user",
            "article",
            "emoji",
            "created_at",
            "updated_at",
        ]

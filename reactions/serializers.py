""" Serializers for blog.reactions """

from rest_framework.serializers import ModelSerializer
from blog.reactions.models import Reaction


# Create your serializers here.
class ReactionSerializer(ModelSerializer):
    """Reaction Serializer"""

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

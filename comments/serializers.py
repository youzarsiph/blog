""" Serializers for blog.comments """

from rest_framework.serializers import ModelSerializer
from blog.comments.models import Comment


# Create your serializers here.
class CommentSerializer(ModelSerializer):
    """Comment Serializer"""

    class Meta:
        """Meta data"""

        model = Comment
        read_only_fields = ["user", "article", "replies"]
        fields = [
            "id",
            "url",
            "user",
            "article",
            "content",
            "replies",
            "created_at",
            "updated_at",
        ]

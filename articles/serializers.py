""" Serializers for blog.articles """

from rest_framework.serializers import ModelSerializer
from blog.articles.models import Article


# Create your serializers here.
class ArticleSerializer(ModelSerializer):
    """Article Serializer"""

    class Meta:
        """Meta data"""

        model = Article
        read_only_fields = ["extras", "user"]
        fields = [
            "id",
            "url",
            "user",
            "photo",
            "title",
            "headline",
            "content",
            "is_pinned",
            "extras",
            "stars",
            "tags",
            "comment_count",
            "reaction_count",
            "tag_count",
            "created_at",
            "updated_at",
        ]

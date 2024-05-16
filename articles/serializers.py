""" Serializers for blog.articles """

from rest_framework.serializers import ModelSerializer
from blog.articles.models import Article


# Create your serializers here.
class ArticleSerializer(ModelSerializer):
    """Article Serializer"""

    class Meta:
        """Meta data"""

        model = Article
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "photo",
            "title",
            "content",
            "is_pinned",
            "tags",
            "created_at",
            "updated_at",
        ]

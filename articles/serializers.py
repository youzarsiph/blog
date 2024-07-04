""" Serializers for blog.articles """

from rest_framework.serializers import ModelSerializer
from blog.articles.models import Article
from blog.users.serializers import UserSerializer


# Create your serializers here.
class ArticleSerializer(ModelSerializer):
    """Article Serializer"""

    user = UserSerializer(read_only=True)

    class Meta:
        """Meta data"""

        model = Article
        read_only_fields = ["extras", "user", "recommendations"]
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
            "recommendations",
            "comment_count",
            "reaction_count",
            "tag_count",
            "created_at",
            "updated_at",
        ]


class ArticleRetrieveSerializer(ArticleSerializer):
    """Article Serializer"""

    class Meta(ArticleSerializer.Meta):
        """Meta data"""

        depth = 1

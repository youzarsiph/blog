""" API endpoints for blog.articles """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.mixins import OwnerMixin
from blog.articles.models import Article
from blog.articles.serializers import ArticleSerializer
from blog.permissions import IsReadOnly
from blog.tags.models import Tag


# Create your views here.
class ArticleViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Articles"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    filterset_fields = ["user", "is_pinned"]
    ordering_fields = ["id", "title", "is_pinned"]


class TagArticlesViewSet(ArticleViewSet):
    """Articles of a tag"""

    permission_classes = [IsAuthenticated, IsReadOnly]

    def get_queryset(self):
        """Filter queryset by tag"""

        tag = Tag.objects.get(id=self.kwargs["id"])
        return super().get_queryset().filter(tags=tag)


class UserArticlesViewSet(ArticleViewSet):
    """Articles of a user"""

    permission_classes = [IsAuthenticated, IsReadOnly]

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)

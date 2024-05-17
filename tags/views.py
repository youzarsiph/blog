""" API endpoints for blog.tags """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from blog.articles.models import Article
from blog.permissions import IsListOnly, IsReadOnly
from blog.tags.models import Tag
from blog.tags.serializers import TagSerializer


# Create your views here.
class TagViewSet(ModelViewSet):
    """Create, read, update and delete Tags"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["name", "color"]
    search_fields = ["name", "description"]
    ordering_fields = ["id", "name", "color", "created_at", "updated_at"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()


class ArticleTagsViewSet(TagViewSet):
    """Tags of an article"""

    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by article"""

        article = Article.objects.get(id=self.kwargs["id"])
        return super().get_queryset().filter(articles=article)

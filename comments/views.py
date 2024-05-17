""" API endpoints for blog.comments """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.mixins import OwnerMixin
from blog.articles.models import Article
from blog.comments.models import Comment
from blog.comments.serializers import CommentSerializer
from blog.permissions import IsListOnly, IsReadOnly


# Create your views here.
class CommentViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Comments"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user", "content"]
    filterset_fields = ["user", "article", "created_at"]
    ordering_fields = ["id", "created_at", "updated_at"]


class ArticleCommentsViewSet(CommentViewSet):
    """Comments of an article"""

    filterset_fields = ["user", "created_at"]

    def perform_create(self, serializer):
        """Perform comment creation"""

        article = Article.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, article=article)

    def get_queryset(self):
        """Filter queryset by article"""

        article = Article.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(article=article)


class UserCommentsViewSet(CommentViewSet):
    """Comments of a user"""

    filterset_fields = ["article", "created_at"]
    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return super().get_queryset().filter(user=self.request.user)

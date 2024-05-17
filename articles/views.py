""" API endpoints for blog.articles """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.mixins import OwnerMixin
from blog.articles.models import Article
from blog.articles.serializers import ArticleSerializer
from blog.permissions import IsListOnly, IsReadOnly
from blog.tags.models import Tag


# Create your views here.
class ArticleViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Articles"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    filterset_fields = ["user", "is_pinned", "tags"]
    ordering_fields = ["id", "title", "is_pinned"]

    @action(methods=["get", "post"], detail=True)
    def react(self, request: Request, pk: int) -> Response:
        """React to an article"""

        message: str
        article = self.get_object()

        if self.request.user not in article.reactions.all():
            article.reactions.add(self.request.user)
            message = f"You reacted to {article} with value"
        else:
            article.reactions.remove(self.request.user)
            message = f"You un-reacted to {article}"

        return Response({"details": message}, status=status.HTTP_200_OK)


class TagArticlesViewSet(ArticleViewSet):
    """Articles of a tag"""

    filterset_fields = ["user", "is_pinned"]
    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by tag"""

        tag = Tag.objects.get(id=self.kwargs["id"])
        return super().get_queryset().filter(tags=tag)


class UserArticlesViewSet(ArticleViewSet):
    """Articles of a user"""

    filterset_fields = ["is_pinned", "tags"]
    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return super().get_queryset().filter(user=self.request.user)

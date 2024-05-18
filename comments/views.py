""" API endpoints for blog.comments """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.mixins import OwnerMixin
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

    @action(methods=["post"], detail=True)
    def reply(self, request: Request, pk: int) -> Response:
        """Reply to a comment"""

        # Get comment object
        obj = self.get_object()

        # Validate and save comment
        serializer = CommentSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        comment = serializer.save(user=request.user, article=obj.article)

        # Add comment to replies
        obj.replies.add(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleCommentsViewSet(CommentViewSet):
    """Comments of an article"""

    filterset_fields = ["user", "created_at"]

    def perform_create(self, serializer):
        """Perform comment creation"""

        serializer.save(user=self.request.user, article_id=self.kwargs["id"])

    def get_queryset(self):
        """Filter queryset by article"""

        return super().get_queryset().filter(article_id=self.kwargs["id"])


class UserCommentsViewSet(CommentViewSet):
    """Comments of a user"""

    filterset_fields = ["article", "created_at"]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return super().get_queryset().filter(user=self.request.user)


class CommentRepliesViewSet(CommentViewSet):
    """Replies of a comment"""

    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by comment"""

        return Comment.objects.get(pk=self.kwargs["id"]).replies.all()

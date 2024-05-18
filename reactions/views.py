""" API endpoints for blog.reactions """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.mixins import OwnerMixin
from blog.permissions import IsListOnly, IsReadOnly
from blog.reactions.models import Reaction
from blog.reactions.serializers import ReactionSerializer


# Create your views here.
class ReactionViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete reactions"""

    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["value"]
    ordering_fields = ["id", "created_at", "updated_at"]
    filterset_fields = ["user", "article"]


class ArticleReactionsViewSet(ReactionViewSet):
    """Reactions of a article"""

    def perform_create(self, serializer):
        """Creates a reaction"""

        serializer.save(user=self.request.user, article_id=self.kwargs["id"])

    def get_queryset(self):
        """Filter queryset by article"""

        return super().get_queryset().filter(article_id=self.kwargs["id"])


class UserReactionsViewSet(ReactionViewSet):
    """Reactions of a user"""

    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return super().get_queryset().filter(user=self.request.user)

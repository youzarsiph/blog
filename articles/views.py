""" API endpoints for blog.articles """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.ai.recsys.views import ArticleRecSysActions
from blog.ai.views import ArticleAIActions
from blog.articles.models import Article
from blog.articles.serializers import ArticleRetrieveSerializer, ArticleSerializer
from blog.followers.models import Follower
from blog.mixins import OwnerMixin
from blog.permissions import IsListOnly, IsReadOnly
from blog.reactions.serializers import ReactionSerializer


# Create your views here.
class ArticleViewSet(OwnerMixin, ArticleAIActions, ArticleRecSysActions, ModelViewSet):
    """Create, read, update and delete Articles"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "headline", "content"]
    filterset_fields = ["user", "is_pinned", "tags"]
    ordering_fields = ["title", "created_at", "updated_at"]

    def get_serializer_class(self):
        """Return different serializer_class based on self.action"""

        match self.action:
            case "react":
                self.serializer_class = ReactionSerializer

            case "retrieve":
                self.serializer_class = ArticleRetrieveSerializer

            case _:
                pass

        return super().get_serializer_class()

    @action(methods=["post"], detail=True)
    def react(self, request: Request, pk: int) -> Response:
        """React to an article"""

        message: str
        # Get article object
        article = self.get_object()

        if self.request.user not in article.reactions.all():
            article.reactions.add(self.request.user)
            message = f"You reacted to {article} with 👍🏻"

        else:
            article.reactions.remove(self.request.user)
            message = f"You un-reacted to {article}"

        return Response({"details": message}, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True)
    def star(self, request: Request, pk: int) -> Response:
        """React to an article"""

        message: str
        # Get article object
        article = self.get_object()

        if self.request.user not in article.stargazers.all():
            article.stargazers.add(self.request.user)
            message = f"{article} starred"

        else:
            article.stargazers.remove(self.request.user)
            message = f"{article} un-starred"

        return Response({"details": message}, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=False)
    def starred(self, request: Request) -> Response:
        """Starred articles"""

        # Get queryset and filter
        queryset = self.filter_queryset(self.get_queryset()).filter(
            stargazers=request.user
        )

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # Return the data
        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def feed(self, request: Request) -> Response:
        """Article feed"""

        # Get queryset and filter
        queryset = self.filter_queryset(self.get_queryset()).filter(
            user__in=[
                f.from_user for f in Follower.objects.filter(to_user=request.user)
            ]
        )

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # Return the data
        return Response(serializer.data)


class TagArticlesViewSet(ArticleViewSet):
    """Articles of a tag"""

    filterset_fields = ["user", "is_pinned"]
    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by tag"""

        return super().get_queryset().filter(tags=self.kwargs["id"])


class UserArticlesViewSet(ArticleViewSet):
    """Articles of a user"""

    filterset_fields = ["is_pinned", "tags"]
    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return super().get_queryset().filter(user_id=self.kwargs["id"])

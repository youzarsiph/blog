""" API endpoints for blog.followers """

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.followers.models import Follower
from blog.followers.serializers import FollowerSerializer
from blog.permissions import IsListOnly, IsReadOnly


# Create your views here.
User = get_user_model()


class FollowerViewSet(ModelViewSet):
    """Create, read, update and delete Followers"""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]
    filterset_fields = ["from_user", "to_user"]
    ordering_fields = ["id", "created_at", "updated_at"]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return (
            super()
            .get_queryset()
            .filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))
        )


class UserFollowersViewSet(FollowerViewSet):
    """Followers of a user"""

    filterset_fields = ["from_user"]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return super().get_queryset().filter(to_user=self.request.user)


class UserFollowingsViewSet(FollowerViewSet):
    """Followings of a user"""

    filterset_fields = ["to_user"]

    def get_queryset(self):
        """Filter queryset by request.user"""

        return super().get_queryset().filter(from_user=self.request.user)

""" API endpoints for blog.followers """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.followers.models import Follower
from blog.followers.serializers import FollowerSerializer


# Create your views here.
class FollowerViewSet(ModelViewSet):
    """Create, read, update and delete Followers"""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at"]
    filterset_fields = ["from_user", "to_user", "is_approved"]

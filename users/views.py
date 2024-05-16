""" API endpoints for blog.users """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from blog.permissions import IsAccountOwner
from blog.users.models import User
from blog.users.serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    """Create, read, update and delete Users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["username", "color"]
    search_fields = ["username", "first_name", "last_name", "bio"]
    ordering_fields = ["id", "username", "first_name", "date_joined", "last_login"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsAccountOwner]

        return super().get_permissions()

""" API endpoints for blog.users """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from blog.permissions import IsAccountOwner
from blog.users.models import User
from blog.users.serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    """Create, read, update and delete Users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["username"]
    search_fields = ["username", "first_name", "last_name", "bio"]
    ordering_fields = ["id", "username", "first_name", "date_joined", "last_login"]

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes += [IsAdminUser]

        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsAccountOwner]

        return super().get_permissions()

    @action(methods=["post"], detail=True)
    def follow(self, request: Request, pk: int) -> Response:
        """Un/Follow a user"""

        message: str
        user = self.get_object()

        if self.request.user not in user.followers.all():
            user.followers.add(self.request.user)
            message = f"You followed {user}"
        else:
            user.followers.remove(self.request.user)
            message = f"You un-followed {user}"

        return Response({"details": message}, status=status.HTTP_200_OK)

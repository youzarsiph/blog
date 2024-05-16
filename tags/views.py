""" API endpoints for blog.tags """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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

""" API endpoints for blog.categories """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from blog.permissions import IsListOnly, IsReadOnly
from blog.categories.models import Category
from blog.categories.serializers import CategorySerializer, CategoryRetrieveSerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    """Create, read, update and delete Categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]

    def get_serializer_class(self):
        """Return different serializer_class based on self.action"""

        match self.action:
            case "retrieve":
                self.serializer_class = CategoryRetrieveSerializer

            case _:
                pass

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes += [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()


class ArticleCategoriesViewSet(CategoryViewSet):
    """Categories of an article"""

    permission_classes = [IsAuthenticated, IsReadOnly, IsListOnly]

    def get_queryset(self):
        """Filter queryset by article"""

        return super().get_queryset().filter(articles=self.kwargs["id"])

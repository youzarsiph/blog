""" API endpoints for blog.reports """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from blog.reports.models import Report
from blog.reports.serializers import ReportSerializer
from blog.mixins import OwnerMixin


# Create your views here.
class ReportViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = ["message"]
    filterset_fields = ["user", "article", "reason"]
    ordering_fields = ["created_at", "updated_at"]

    def get_permissions(self):
        """Allow users to create reports"""

        if self.action == "create":
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()


class ArticleReportsViewSet(ReportViewSet):
    """Reports of an article"""

    def perform_create(self, serializer):
        """Perform comment creation"""

        serializer.save(user=self.request.user, article_id=self.kwargs["id"])

    def get_queryset(self):
        """Filter queryset by article"""

        return super().get_queryset().filter(article_id=self.kwargs["id"])

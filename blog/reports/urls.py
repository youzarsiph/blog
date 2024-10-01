""" URLConf for blog.reports """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.reports.views import ArticleReportsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("reports", ArticleReportsViewSet, "report")

urlpatterns = [
    path(
        "articles/<int:id>/",
        include((router.urls, "reports"), namespace="reports"),
    ),
]

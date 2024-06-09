""" URLConf for blog.tags """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.articles.views import TagArticlesViewSet


# Create your URLConf here.
router = DefaultRouter()
router.register("articles", TagArticlesViewSet, "article")

urlpatterns = [
    path("tags/<int:id>/", include((router.urls, "tags"), namespace="tags")),
]

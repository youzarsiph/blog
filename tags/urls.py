""" URLConf for blog.tags """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.articles.views import TagArticlesViewSet
from blog.tags.views import TagViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("tags", TagViewSet, "tag")

sub_router = DefaultRouter()
sub_router.register("articles", TagArticlesViewSet, "article")

urlpatterns = [
    path("", include(router.urls)),
    path("tags/<int:id>/", include((sub_router.urls, "tags"), namespace="tags")),
]

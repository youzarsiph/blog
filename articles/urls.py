""" URLConf for blog.articles """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.comments.views import ArticleCommentsViewSet
from blog.articles.views import ArticleViewSet
from blog.reactions.views import ArticleReactionsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("articles", ArticleViewSet, "article")

sub_router = DefaultRouter()
sub_router.register("comments", ArticleCommentsViewSet, "comment")
sub_router.register("reactions", ArticleReactionsViewSet, "reaction")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "articles/<int:id>/",
        include((sub_router.urls, "articles"), namespace="articles"),
    ),
]

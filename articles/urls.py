""" URLConf for blog.articles """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.comments.views import ArticleCommentsViewSet
from blog.reactions.views import ArticleReactionsViewSet
from blog.tags.views import ArticleTagsViewSet

# Create your URLConf here.
router = DefaultRouter()
router.register("comments", ArticleCommentsViewSet, "comment")
router.register("reactions", ArticleReactionsViewSet, "reaction")
router.register("tags", ArticleTagsViewSet, "tag")


urlpatterns = [
    path(
        "articles/<int:id>/",
        include((router.urls, "articles"), namespace="articles"),
    ),
]

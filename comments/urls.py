""" URLConf for blog.comments """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.comments.views import CommentRepliesViewSet, UserCommentsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("comments", UserCommentsViewSet, "comment")

sub_router = DefaultRouter()
sub_router.register("replies", CommentRepliesViewSet, "reply")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "comments/<int:id>/",
        include((sub_router.urls, "comments"), namespace="comments"),
    ),
]

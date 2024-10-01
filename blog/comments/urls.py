""" URLConf for blog.comments """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.comments.views import CommentRepliesViewSet


# Create your URLConf here.
router = DefaultRouter()
router.register("replies", CommentRepliesViewSet, "reply")

urlpatterns = [
    path(
        "comments/<int:id>/",
        include((router.urls, "comments"), namespace="comments"),
    ),
]

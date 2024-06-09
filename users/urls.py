""" URLConf for blog.users """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.articles.views import UserArticlesViewSet
from blog.followers.views import UserFollowersViewSet, UserFollowingViewSet


# Create your URLConf here.
router = DefaultRouter()
router.register("articles", UserArticlesViewSet, "article")
router.register("followers", UserFollowersViewSet, "follower")
router.register("following", UserFollowingViewSet, "following")

urlpatterns = [
    path("users/<int:id>/", include((router.urls, "users"), namespace="users")),
]

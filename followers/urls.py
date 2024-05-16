""" URLConf for blog.followers """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.followers.views import FollowerViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("followers", FollowerViewSet, "follower")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]

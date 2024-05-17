""" URLConf for blog.users """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.articles.views import UserArticlesViewSet
from blog.users.views import UserViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, "user")

sub_router = DefaultRouter()
sub_router.register("articles", UserArticlesViewSet, "article")

urlpatterns = [
    path("", include(router.urls)),
    path("users/<int:id>/", include((sub_router.urls, "users"), namespace="users")),
]

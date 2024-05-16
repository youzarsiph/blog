""" URLConf for blog.users """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from blog.users.views import TagViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("users/<int:id>/", include((sub_router.urls, "users"), namespace="users")),
]

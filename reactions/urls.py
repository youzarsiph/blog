""" URLConf for blog.reactions """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.reactions.views import ReactionViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("reactions", ReactionViewSet, "reaction")


urlpatterns = [
    path("", include(router.urls)),
]

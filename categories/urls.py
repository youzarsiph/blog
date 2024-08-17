""" URLConf for blog.categories """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.articles.views import CategoryArticlesViewSet


# Create your URLConf here.
router = DefaultRouter()
router.register("articles", CategoryArticlesViewSet, "article")

urlpatterns = [
    path(
        "categories/<int:id>/",
        include((router.urls, "categories"), namespace="categories"),
    ),
]

""" URLConf for blog """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.articles.views import ArticleViewSet
from blog.categories.views import CategoryViewSet
from blog.comments.views import CommentViewSet
from blog.followers.views import FollowerViewSet
from blog.reactions.views import ReactionViewSet
from blog.reports.views import ReportViewSet
from blog.tags.views import TagViewSet
from blog.users.views import UserViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("articles", ArticleViewSet, "article")
router.register("categories", CategoryViewSet, "category")
router.register("comments", CommentViewSet, "comment")
router.register("followers", FollowerViewSet, "follower")
router.register("reactions", ReactionViewSet, "reaction")
router.register("reports", ReportViewSet, "report")
router.register("tags", TagViewSet, "tag")
router.register("users", UserViewSet, "user")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("blog.articles.urls")),
    path("", include("blog.categories.urls")),
    path("", include("blog.comments.urls")),
    path("", include("blog.reports.urls")),
    path("", include("blog.tags.urls")),
    path("", include("blog.users.urls")),
]

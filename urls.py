""" URLConf for blog """

from django.urls import path, include


# Create your URLConf here.
urlpatterns = [
    path("", include("blog.articles.urls")),
    path("", include("blog.comments.urls")),
    path("", include("blog.followers.urls")),
    path("", include("blog.reactions.urls")),
    path("", include("blog.tags.urls")),
    path("", include("blog.users.urls")),
]

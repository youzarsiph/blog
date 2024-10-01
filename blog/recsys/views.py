""" API endpoints for blog.recsys """

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response


# Create your views here.
class ArticleRecSysActions:
    """Explore articles and recommendations"""

    @action(methods=["get"], detail=True)
    def recommendations(self, request: Request, pk: int) -> Response:
        """Recommend similar articles using Content Based Filtering"""

        # Get the article
        article = self.get_object()

        # Get queryset and filter
        queryset = self.filter_queryset(article.recommendations.all())

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # Return the data
        return Response(serializer.data)

""" API endpoints for blog.ai.recsys """

import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from blog.articles.models import Article
from blog.reactions.models import Reaction
from blog.users.models import User


# Create your views here.
class ArticleRecSysActions:
    """Explore articles and recommendations"""

    @action(methods=["get", "post"], detail=False)
    def explore(self, request: Request) -> Response:
        """Recommended articles for current user using Collaborative Filtering Algorithm"""

        # Get all articles
        articles = Article.objects.all()

        # Create a data-frame to store the reactions of each user to each article
        data = pd.DataFrame(index=articles, columns=User.objects.all())
        for article in articles:
            for reaction in Reaction.objects.filter(article=article):
                data.loc[article, reaction.user] = 1

        # Fill missing values with 0
        data.fillna(0, inplace=True)

        # Standardize the data
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data.T)

        # Compute the cosine similarity matrix
        similarity_matrix = cosine_similarity(data_scaled)

        # Get the reactions of the current user
        user_reactions = Reaction.objects.filter(user=request.user)

        # Compute the scores for each article
        scores = similarity_matrix.dot(
            np.array([reaction.article.id for reaction in user_reactions])
        ) / np.array([np.abs(similarity_matrix).sum(axis=1)])

        # Get the indices of the articles sorted by their scores
        top_indices = np.argsort(scores)[::-1]

        # Get queryset and filter
        queryset = self.filter_queryset(articles.filter(id__in=top_indices))

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # Return the data
        return Response(serializer.data)

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

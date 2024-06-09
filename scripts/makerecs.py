""" Blog Make Recommendations: A script for computing recommendations using Content Based Filtering algorithm """

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from blog.articles.models import Article


def run() -> None:
    """Compute article recommendations"""

    print("Computing recommendations")

    # Article data
    df = pd.DataFrame(
        [
            {
                "id": article.pk,
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at,
                "updated_at": article.updated_at,
            }
            for article in Article.objects.all()
        ]
    )

    # Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(
        [
            f"{a[1]}\n\nDate published: {a[3]}, Last update: {a[4]}\n{a[2]}"
            for a in df.values
        ]
    )

    # Compute similar articles
    similar_articles = cosine_similarity(matrix)

    # Add recommendations to data-frame
    df["recommendations"] = [
        df["id"].loc[x.argsort()[-5:-1]].tolist() for x in similar_articles
    ]

    # Add recommendations to database
    for a in df[["id", "recommendations"]].values:
        # Get article
        article = Article.objects.get(id=a[0])

        # Clear recommendations
        article.recommendations.clear()

        # Add recommended articles
        for i in a[1]:
            article.recommendations.add(i)

    print("All Done")

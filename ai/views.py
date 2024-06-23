""" API endpoints for blog.ai """

from huggingface_hub import InferenceClient
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from blog.ai import serializers
from blog.ai.utils.text import clean_output


# Create your views here.
class ArticleAIActions:
    """AI actions for articles"""

    client = InferenceClient()

    def get_serializer_class(self):
        """Return different serializer_class for different actions"""

        match self.action:
            case "article_generation":
                self.serializer_class = serializers.TextGenerationSerializer

            case "qa":
                self.serializer_class = serializers.QuestionAnsweringSerializer

            case "translation":
                self.serializer_class = serializers.TranslationSerializer

            case "summarization":
                self.serializer_class = serializers.BaseSerializer

        return super().get_serializer_class()

    @action(methods=["post"], detail=False, url_path="article-generation")
    def article_generation(self, request: Request) -> Response:
        """Generate an article"""

        # Get the serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "article": self.client.text_generation(
                    prompt=serializer.validated_data["prompt"],
                    model=serializer.validated_data["model"],
                )
            },
        )

    @action(methods=["post"], detail=True)
    def summarization(self, request: Request, pk: int) -> Response:
        """Summarize an article"""

        # Get article object
        article = self.get_object()

        # Get the serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Summarize article
        return Response(
            {
                "summary": clean_output(
                    self.client.summarization(
                        text=f"{article.title}\n{article.headline}\n{article.content}",
                        model=serializer.validated_data["model"],
                    ).summary_text
                )
            },
        )

    @action(methods=["post"], detail=True, url_path="translation")
    def translation(self, request: Request, pk: int) -> Response:
        """Translate an article"""

        # Get article object
        article = self.get_object()

        # Get the serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Translate article
        return Response(
            {
                "translation": self.client.translation(
                    text=f"{article.title} {article.content}",
                    src_lang=serializer.validated_data["source"],
                    tgt_lang=serializer.validated_data["target"],
                    model=serializer.validated_data["model"],
                ).translation_text
            },
        )

    @action(methods=["post"], detail=True, url_path="qa")
    def qa(self, request: Request, pk: int) -> Response:
        """Answer question using data form this article"""

        # Get article object
        article = self.get_object()

        # Get the serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "question": serializer.validated_data["question"],
                "answer": self.client.question_answering(
                    question=serializer.validated_data["question"],
                    context=f"{article.title} {article.content}",
                    model=serializer.validated_data["model"],
                ),
            },
        )


class CommentAIActions:
    """AI actions for comments"""

    client = InferenceClient()

    def get_serializer_class(self):
        """Return different serializer_class for different actions"""

        match self.action:
            case "summarization":
                self.serializer_class = serializers.BaseSerializer

            case "sentiment_analysis":
                self.serializer_class = serializers.BaseSerializer

            case "translation":
                self.serializer_class = serializers.TranslationSerializer

        return super().get_serializer_class()

    @action(methods=["post"], detail=True)
    def summarization(self, request: Request, pk: int) -> Response:
        """Summarize a comment"""

        # Get comment object
        comment = self.get_object()

        # Summarize comment
        return Response(
            {
                "summary": clean_output(
                    self.client.summarization(f"{comment.content}").summary_text
                )
            },
        )

    @action(methods=["post"], detail=True, url_path="translation")
    def translation(self, request: Request, pk: int) -> Response:
        """Translate a comment"""

        # Get comment object
        comment = self.get_object()

        # Get source and target languages
        src = request.POST.get("src", None)
        target = request.POST.get("target", None)

        if src is None or target is None:
            return Response(
                {"details": "The src/target fields are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Translate comment
        return Response(
            {
                "translation": self.client.translation(
                    text=f"{comment.content}",
                    src_lang=src,
                    tgt_lang=target,
                    model="Helsinki-NLP/opus-mt-en-fr",
                ).translation_text
            },
        )

    @action(methods=["post"], detail=True, url_path="sentiment-analysis")
    def sentiment_analysis(self, request: Request, pk: int) -> Response:
        """Analyze comment sentiment"""

        # Get comment object
        comment = self.get_object()

        return Response(
            {
                "result": self.client.text_classification(comment.content),
            },
        )

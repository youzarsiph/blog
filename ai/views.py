""" API endpoints for blog.ai """

from huggingface_hub import InferenceClient
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from blog.ai import serializers


# Create your views here.
class ArticleAIActions:
    """AI actions for articles"""

    client = InferenceClient()

    def get_serializer_class(self):
        """Return different serializer_class for different actions"""

        match self.action:
            case "article_generation":
                self.serializer_class = serializers.ChatSerializer

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

        messages = [
            {
                "role": "system",
                "content": """
                Welcome to the AI Article Generator! I am here to assist you in creating high-quality articles on a wide range of topics.
                Whether you need content for your blog, website, or any other platform, I can help you generate engaging and informative articles tailored to your needs.\n\n**Features:**
                - **Topic Selection:** Provide a topic or let me suggest one for you.
                - **Content Customization:** Specify the tone, style, and length of the article.
                - **Keyword Optimization:** Include keywords to enhance SEO.
                - **Multiple Drafts:** Generate multiple drafts to choose from.
                - **Editing Assistance:** Get help with grammar, punctuation, and structure.\n\n**How to Use:**
                1. **Start a Conversation:** Begin by telling me the topic or type of article you need.
                2. **Provide Details:** Share any specific requirements or preferences you have.
                3. **Review Drafts:** I will generate drafts for you to review and select.
                4. **Finalize:** Make any necessary edits and finalize your article.\n\nLet's get started! What topic would you like to write about today?""",
            },
            {
                "role": "user",
                "content": serializer.validated_data["message"],
            },
        ]

        return Response(
            {
                "article": self.client.chat_completion(
                    messages=messages,
                    model=serializer.validated_data.get("model"),
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
                "summary": self.client.summarization(
                    text=f"{article.title}\n{article.headline}\n{article.content}",
                    model=serializer.validated_data.get("model"),
                ).summary_text
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
                    model=serializer.validated_data.get("model"),
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
                    model=serializer.validated_data.get("model"),
                ),
            },
        )


class CommentAIActions:
    """AI actions for comments"""

    client = InferenceClient()

    def get_serializer_class(self):
        """Return different serializer_class for different actions"""

        match self.action:
            case "summarization" | "sentiment_analysis":
                self.serializer_class = serializers.BaseSerializer

            case "translation":
                self.serializer_class = serializers.TranslationSerializer

        return super().get_serializer_class()

    @action(methods=["post"], detail=True)
    def summarization(self, request: Request, pk: int) -> Response:
        """Summarize a comment"""

        # Get comment object
        comment = self.get_object()

        # Get the serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Summarize comment
        return Response(
            {"summary": self.client.summarization(comment.content).summary_text},
        )

    @action(methods=["post"], detail=True, url_path="translation")
    def translation(self, request: Request, pk: int) -> Response:
        """Translate a comment"""

        # Get comment object
        comment = self.get_object()

        # Get the serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Translate comment
        return Response(
            {
                "translation": self.client.translation(
                    text=comment.content,
                    src_lang=serializer.validated_data["source"],
                    tgt_lang=serializer.validated_data["target"],
                    model=serializer.validated_data.get("model"),
                ).translation_text
            },
        )

    @action(methods=["post"], detail=True, url_path="sentiment-analysis")
    def sentiment_analysis(self, request: Request, pk: int) -> Response:
        """Analyze comment sentiment"""

        # Get comment object
        comment = self.get_object()

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
                "result": self.client.text_classification(comment.content),
            },
        )

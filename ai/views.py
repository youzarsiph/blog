""" API endpoints for blog.ai """

from huggingface_hub import InferenceClient
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from blog.ai.utils.text import clean_output


# TOKEN = os.environ["HF_TOKEN"]
TOKEN = "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"


# Create your views here.
class ArticleAIActions:
    """AI actions for articles"""

    client = InferenceClient(token=TOKEN)

    @action(methods=["get", "post"], detail=False)
    def generate(self, request: Request) -> Response:
        """Generate an article"""

        # Get the prompt
        prompt = request.POST.get("prompt", None)

        if prompt is None:
            return Response(
                {"details": "The prompt field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "article": self.client.text_generation(
                    prompt,
                    max_new_tokens=4096,
                )
            },
        )

    @action(methods=["get", "post"], detail=True, url_path="summary")
    def summary(self, request: Request, pk: int) -> Response:
        """Summarize an article"""

        # Get article object
        article = self.get_object()

        # Summarize article
        return Response(
            {
                "summary": clean_output(
                    self.client.summarization(
                        f"{article.title} {article.content}"
                    ).summary_text
                )
            },
        )

    @action(methods=["get", "post"], detail=True, url_path="translation")
    def translation(self, request: Request, pk: int) -> Response:
        """Translate an article"""

        # Get article object
        article = self.get_object()

        # Get source and target languages
        src = request.POST.get("src", None)
        target = request.POST.get("target", None)

        if src is None or target is None:
            return Response(
                {"details": "The src/target fields are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Translate article
        return Response(
            {
                "translation": self.client.translation(
                    text=f"{article.title} {article.content}",
                    src_lang=src,
                    tgt_lang=target,
                    model="Helsinki-NLP/opus-mt-en-fr",
                ).translation_text
            },
        )

    @action(methods=["get", "post"], detail=True, url_path="qa")
    def qa(self, request: Request, pk: int) -> Response:
        """Answer question using data form this article"""

        # Get article object
        article = self.get_object()

        # Get question
        question = request.POST.get("question", None)

        if question is None:
            return Response(
                {"details": "The question field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "question": "What is Clustering?",
                "answer": self.client.question_answering(
                    question="What is Clustering?",
                    context=f"{article.title} {article.content}",
                ),
            },
        )


class CommentAIActions:
    """AI actions for comments"""

    client = InferenceClient(token=TOKEN)

    @action(methods=["get", "post"], detail=True, url_path="summary")
    def summary(self, request: Request, pk: int) -> Response:
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

    @action(methods=["get", "post"], detail=True, url_path="translation")
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

    @action(methods=["get", "post"], detail=True, url_path="sentiment-analysis")
    def sentiment_analysis(self, request: Request, pk: int) -> Response:
        """Analyze comment sentiment"""

        # Get comment object
        comment = self.get_object()

        return Response(
            {
                "result": self.client.text_classification(comment.content),
            },
        )

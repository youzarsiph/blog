from blog.models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import get_user_model
from blog.views.generic import MessageRequiredDeletionView, RequestUser, LoginRequiredMixin, AuthorityRequiredMixin

User = get_user_model()


class UserDeletionView(LoginRequiredMixin, RequestUser, MessageRequiredDeletionView):
    model = User
    success_url = reverse_lazy('blog:index')
    success_message = 'Account deleted successfully.'
    error_message = 'Error occurred while processing.'


class PostDeletionView(AuthorityRequiredMixin, MessageRequiredDeletionView):
    model = Post
    success_url = reverse_lazy('blog:dashboard')


class CommentDeletionView(AuthorityRequiredMixin, MessageRequiredDeletionView):
    model = Comment
    success_url = reverse_lazy('blog:dashboard')

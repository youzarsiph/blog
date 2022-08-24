from django.urls import reverse_lazy
from blog.models import Post, Comment
from django.contrib.auth import get_user_model
from blog.forms.create import StyledUserCreationForm, PostCreationForm, CommentCreationForm
from blog.views.generic import CreationView, UserRequiredMixin, MessageRequiredCreationView

User = get_user_model()


class UserCreationView(CreationView):
    model = User
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('blog:login')

    def get_success_url(self):
        return reverse_lazy('blog:edit_user', args=[self.object.pk])


class PostCreationView(UserRequiredMixin, MessageRequiredCreationView):
    model = Post
    form_class = PostCreationForm
    success_url = reverse_lazy('blog:dashboard')


class CommentCreationView(UserRequiredMixin, MessageRequiredCreationView):
    model = Comment
    form_class = CommentCreationForm

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.object.post.id])

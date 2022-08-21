from blog.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import get_user_model
from blog.forms.main import UserEditForm, PostCreationForm, CommentCreationForm
from blog.views.generic import MessageRequiredEditView, RequestUser, LoginRequiredMixin, AuthorityRequiredMixin

User = get_user_model()


class UserEditView(LoginRequiredMixin, RequestUser, MessageRequiredEditView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('blog:profile')
    success_message = 'Account updated successfully.'
    error_message = 'Error occurred while processing.'

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if not (user.first_name and user.last_name and user.email):
            messages.success(request, 'Account created successfully, please fill in your information.')
        return super().get(request, *args, **kwargs)


class PostEditView(AuthorityRequiredMixin, MessageRequiredEditView):
    model = Post
    form_class = PostCreationForm

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.object.pk])


class CommentEditView(AuthorityRequiredMixin, MessageRequiredEditView):
    model = Comment
    form_class = CommentCreationForm

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.object.pk])

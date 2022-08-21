from blog.views.list import *
from blog.views.edit import *
from blog.views.create import *
from blog.views.detail import *
from blog.views.delete import *
from django.views.generic import TemplateView
from blog.views.mixins import LoginRequiredMixin


# Create your views here.
class IndexView(TemplateView):
    template_name = 'blog/base/index.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/base/dashboard.html'

    def get_context_data(self, **kwargs):
        self.extra_context = {
            'comment_form': CommentCreationForm(),
            'post_list': Post.objects.all().filter(user=self.request.user),
        }
        return super().get_context_data(**kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/authentication/profile.html'

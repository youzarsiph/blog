from blog.models import *
from blog.views.generic import DetailsView
from blog.forms.create import CommentCreationForm


class PostDetailView(DetailsView):
    model = Post
    extra_context = {
        'comment_form': CommentCreationForm()
    }

from blog.models import Post
from blog.views.generic import ListingView
from blog.forms.create import CommentCreationForm


class PostListView(ListingView):
    model = Post
    extra_context = {
        'comment_form': CommentCreationForm()
    }

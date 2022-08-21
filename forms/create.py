from blog.models import *
from blog.forms.base import StyledModelForm
from django.contrib.auth.views import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(StyledUserCreationForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            field = self.fields[label]
            try:
                if field.widget.input_type == 'checkbox' or field.widget.input_type == 'radio':
                    field.widget.attrs['class'] = 'form-check-input'
                else:
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label
            except Exception:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label


class PostCreationForm(StyledModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class CommentCreationForm(StyledModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'post')

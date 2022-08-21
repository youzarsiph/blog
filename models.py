from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class BaseModel:
    """
    A mixin class to provide get_absolute_url method to model classes following the convention.
    Requires ListView names to be modelName_list.
    """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        suffix = self._meta.verbose_name.lower()
        return reverse_lazy('blog:' + suffix + '_list')


# Create your models here.
class BlogUser(AbstractUser):
    bio = models.CharField(
        max_length=256,
        help_text='Tell us about yourself'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/users/'
    )


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/posts/'
    )
    title = models.CharField(
        max_length=128,
        unique=True,
        help_text='The title for your post'
    )
    content = models.TextField(
        help_text='The content of your post'
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(
        help_text='The content of your comment'
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

from django.urls import path
from blog.forms.main import *
from blog.views.main import *
from django.urls import reverse_lazy
from django.contrib.auth import views
from blog.views.generic import ModelImageView

app_name = 'blog'

patterns = [
    # Main views
    path('', IndexView.as_view(), name='index'),
    path('dashbaord/', DashboardView.as_view(), name='dashboard'),
    path('users/<int:pk>/image/', ModelImageView.as_view(model=User), name='user_image'),

    # Posts
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/', PostCreationView.as_view(), name='create_post'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:id>/edit/', PostEditView.as_view(), name='edit_post'),
    path('posts/<int:id>/delete/', PostDeletionView.as_view(), name='delete_post'),
    path('posts/<int:pk>/image/', ModelImageView.as_view(model=Post), name='post_image'),

    # Comments
    path('comments/new/', CommentCreationView.as_view(), name='create_comment'),
    path('comments/<int:id>/edit/', CommentEditView.as_view(), name='edit_comment'),
    path('commnets/<int:id>/delete/', CommentDeletionView.as_view(), name='delete_comment'),
]

auth = [  # Custom authentication patterns
    path(
        'accounts/login/',
        views.LoginView.as_view(
            form_class=StyledAuthenticationForm,
            template_name='blog/authentication/login.html',
            extra_context={
                'signup_form': StyledUserCreationForm()
            }
        ),
        name='login'
    ),
    path(
        'accounts/register/',
        UserCreationView.as_view(),
        name='register'
    ),
    path(
        'accounts/<int:id>/edit/',
        UserEditView.as_view(),
        name='edit_user'
    ),
    path(
        'accounts/<int:id>/delete/',
        UserDeletionView.as_view(),
        name='delete_user'
    ),
    path(
        'accounts/logout/',
        views.LogoutView.as_view(
            template_name='blog/authentication/logged_out.html'
        ),
        name='logout'
    ),
    path(
        'accounts/profile/',
        ProfileView.as_view(),
        name='profile'
    ),
    path(
        'accounts/password/change/',
        views.PasswordChangeView.as_view(
            form_class=StyledPasswordChangeForm,
            template_name='blog/authentication/change_password.html',
            success_url=reverse_lazy('blog:change_done')
        ),
        name='change_password'
    ),
    path(
        'accounts/password/change/done/',
        views.PasswordChangeDoneView.as_view(
            template_name='blog/authentication/change_done.html'
        ),
        name='change_done'
    ),
    path(
        'accounts/password/reset/',
        views.PasswordResetView.as_view(
            form_class=StyledPasswordResetForm,
            template_name='blog/authentication/reset_password.html',
            success_url=reverse_lazy('blog:reset_done')
        ),
        name='reset_password'
    ),
    path(
        'accounts/password/reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='blog/authentication/reset_done.html'
        ),
        name='reset_done'
    ),
    path(
        'accounts/password/reset/confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='blog/authentication/reset_confirm.html',
            form_class=StyledPasswordResetForm,
            success_url=reverse_lazy('blog:reset_complete')
        ),
        name='reset_confirm'
    ),
    path(
        'accounts/password/reset/complete/',
        views.PasswordResetCompleteView.as_view(
            template_name='blog/authentication/reset_complete.html',
        ),
        name='reset_complete'
    ),
]

urlpatterns = patterns + auth

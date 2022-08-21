from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class DashboardMixin(LoginRequiredMixin, PermissionRequiredMixin):
    pass


class MessageMixin:
    """
    Base mixin class to add success and error messages.
    """
    action = 'created'
    success_message = '{} was {} successfully.'
    error_message = 'An error occurred while processing.'

    def get_success_message(self):
        return self.success_message.format(self.model._meta.verbose_name.title().capitalize(), self.action)

    def get_error_message(self):
        return self.error_message


class MessageMixinCreateView(MessageMixin):
    """
    A mixin for CreateView to set success and error messages.
    """

    def post(self, request, *args, **kwargs):
        try:
            response = super(MessageMixinCreateView, self).post(request, *args, **kwargs)
            messages.success(request, self.get_success_message())
            return response
        except Exception as error:
            raise error


class MessageMixinUpdateView(MessageMixin):
    """
    A mixin for UpdateView to set success and error messages.
    """
    action = 'updated'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, self.get_success_message())
        return super().post(request, *args, **kwargs)


class MessageMixinDeleteView(MessageMixin):
    """
    A mixin for DeleteView to set success and error messages.
    """
    action = 'deleted'

    def post(self, request, *args, **kwargs):
        messages.success(request, self.get_success_message())
        return self.delete(request, *args, **kwargs)


class UserRequiredMixin(LoginRequiredMixin):
    """
    A mixin for CreateView to set the owner of the object.
    """

    def form_valid(self, form):
        """ Set the owner of the object. """
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(UserRequiredMixin, self).form_valid(form)


class AuthorityRequiredMixin(LoginRequiredMixin):
    """
    A mixin for UpdateView, DetailView and ListView to limit the user to only modifying or viewing their own data.
    """

    def get_queryset(self):
        """ Limit a User to only modifying or viewing their own data. """
        query_set = super(AuthorityRequiredMixin, self).get_queryset()
        return query_set.filter(user=self.request.user)


class RequestUser(UserPassesTestMixin):
    """
    A mixin for UpdateView, DeleteView and DetailView to limit the user to only modifying or viewing their
    own user object. In other words, the current logged in user can edit their account only.
    """

    def test_func(self):
        return self.request.user == self.get_object()


class SuperUserRequiredMixin(UserPassesTestMixin):
    """
    Verify that the current user is superuser.
    """

    def test_func(self):
        return self.request.user.is_superuser


class StaffUserRequiredMixin(UserPassesTestMixin):
    """
    Verify that the current user is staff.
    """

    def test_func(self):
        return self.request.user.is_staff


class TemplateNameMixin:
    """
    A mixin to set the template_name and it's extension.
    """
    app_name = 'blog'
    parent_dir = ''
    extension = ''

    def get_template_names(self):
        template = self.app_name + '/views/' + self.parent_dir + self.model._meta.verbose_name.title().lower()
        template += self.extension
        return [template]

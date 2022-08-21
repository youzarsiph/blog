from django.views import View
from blog.views.mixins import *
from django.http import FileResponse
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


class CreationView(TemplateNameMixin, CreateView):
    """
    CreateView with template set automatically according to folder structure.
    """
    parent_dir = 'create/'
    extension = '.html'


class DetailsView(TemplateNameMixin, DetailView):
    """
    DetailView with template set automatically according to folder structure.
    """
    pk_url_kwarg = 'id'
    parent_dir = 'detail/'
    extension = '.html'


class ListingView(TemplateNameMixin, ListView):
    """
    ListView with template set automatically according to folder structure.
    """
    parent_dir = 'list/'
    extension = '.html'


class EditView(TemplateNameMixin, UpdateView):
    """
    UpdateView with template set automatically according to folder structure.
    """
    pk_url_kwarg = 'id'
    parent_dir = 'edit/'
    extension = '.html'


class DeletionView(TemplateNameMixin, DeleteView):
    """
    DeleteView with template set automatically according to folder structure.
    """
    pk_url_kwarg = 'id'
    parent_dir = 'delete/'
    extension = '.html'

    def get_success_url(self):
        return reverse_lazy('blog:' + self.model._meta.verbose_name.lower() + '_list')


# Generic Views with Messages
class MessageRequiredCreationView(MessageMixinCreateView, CreationView):
    """
    CreationView with messages.
    You need to define success_message and error_message in subclasses.
    """


class MessageRequiredEditView(MessageMixinUpdateView, EditView):
    """
    EditView with messages.
    You need to define success_message and error_message in subclasses.
    """


class MessageRequiredDeletionView(MessageMixinDeleteView, DeletionView):
    """
    DeletionView with messages.
    You need to define success_message and error_message in subclasses.
    """


class ModelImageView(View):
    """
    A view that serves user uploaded images.
    """
    model = None

    def get(self, request, pk):
        if self.model is not None:
            obj = self.model.objects.get(id=pk)
            return FileResponse(open(obj.image.url[1:], 'rb'), as_attachment=True)
        else:
            raise ImproperlyConfigured('You need to configure the model field.')

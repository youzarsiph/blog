from blog.forms.edit import *
from blog.forms.create import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, PasswordResetForm


class StyledForm:
    """
    A class to provide styles to input tags.
    """

    def __init__(self, *args, **kwargs):
        super(StyledForm, self).__init__(*args, **kwargs)
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


class StyledPasswordChangeForm(StyledForm, PasswordChangeForm):
    pass


UserModel = get_user_model()


class StyledAuthenticationForm(AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        super(AuthenticationForm, self).__init__(*args, **kwargs)
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


class StyledPasswordResetForm(StyledForm, PasswordResetForm):
    pass

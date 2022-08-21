from django import forms


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StyledModelForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            field = self.fields[label]
            try:
                if field.widget.input_type == 'checkbox' or field.widget.input_type == 'radio':
                    field.widget.attrs['class'] = 'form-check-input'
                elif field.widget.input_type == 'select':
                    field.widget.attrs['class'] = 'form-select'
                    field.widget.attrs['placeholder'] = field.label
                else:
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label
            except Exception:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label

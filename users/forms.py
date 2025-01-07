from django import forms

from users.models import User

class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserLoginForm(StyleFromMixin, forms.Form):
    """ Форма для авторизации пользователя."""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
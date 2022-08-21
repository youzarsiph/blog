# Blog

A reusable blog app written in python and django.

# Get Started

Start a project:

```shell
django-admin startproject mysite
cd mysite
```

Clone the repo using git:

```shell
git clone https://github.com/youzarsiph/blog.git
```

Install blog, in `mysite/settings.py`:

```python
INSTALLED_APPS = [
    'blog.apps.BlogConfig',  # Add this line
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Include `urls.py` from the JApp, in `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include  # import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Add this line
]
```

Run migrate command:

```shell
python manage.py migrate
```

Run the server:

```shell
python manage.py runserver
```

Blog uses Django's default user model by default, but it comes with its own custom user model. If you want to use Blog's
user model follow this steps:

First open `mysite/sttings.py` file:

```python
...
DEBUG = True

# Add this line
AUTH_USER_MODEL = 'blog.BlogUser'
...
```

Then open `blog/forms/edit.py` file:

```python
from blog.models import *
from blog.forms.base import StyledModelForm
from django.contrib.auth.views import get_user_model

User = get_user_model()


class UserEditForm(StyledModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            # Uncomment following lines
            # 'bio',
            # 'image'
        )
```

Now Blog uses its own user model.

I hope you find this useful.

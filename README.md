# Blog

[![Django CI](https://github.com/youzarsiph/blog/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/blog/actions/workflows/django.yml)
[![Black](https://github.com/youzarsiph/blog/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/blog/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/blog/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/blog/actions/workflows/ruff.yml)

Blog API built using Python, Django and DRF.

## Get started

Install django:

```console
pip install django
```

Create a new project:

```console
python -m django startproject mysite
cd mysite
```

Clone the repo:

```console
git clone https://github.com/youzarsiph/blog
```

Install dependencies:

```console
pip install -r blog/requirements.txt
```

Use `blog`'s custom User model, in `mysite/settings.py`:

```python
AUTH_USER_MODEL = 'users.User'  # Add this line
```

Configure the settings, in `mysite/settings.py`:

```python
...

INSTALLED_APPS = [
    # Add the following lines
    "blog",
    "blog.ai",
    "blog.ai.recsys",
    "blog.articles",
    "blog.comments",
    "blog.followers",
    "blog.reactions",
    "blog.tags",
    "blog.users",
    "corsheaders",
    "drf_redesign",  # Makes the API interface prettier
    "rest_framework",  # REST Framework
    "rest_framework.authtoken",  # DRF Token authentication
    "django_filters",  # For filtering support
    "django_extensions",  # For running script that computes recommendations
    ...
]

...

# DRF configuration
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
}

CORS_ALLOW_ALL_ORIGINS = True
```

Add `blog` to `URLConf`, in `mysite/urls.py`:

```python
from django.urls import path, include


urlpatterns = [
    # Add the following lines
    path("", include("blog.urls")),
    path("auth/", include("rest_framework.urls")),
]
```

Run migrations:

```console
python manage.py migrate
```

Generate an auth token:

```bash
# Optional create a superuser
# python manage.py createsuperuser
python manage.py drf_create_token <YOUR_USERNAME>
```

Run `makerecs` to compute recommendations:

```console
python manage.py runscript makerecs
```

Create a file named `.env` and add your [HuggingFace Token](https://huggingface.co), if you want to use the AI services:

```txt
HF_TOKEN=hf_**********************************
```

## Project Structure

The app consists of the following sub apps:

- `ai`: Provides extra actions for articles and comments like summarization, sentiment analysis etc...
- `ai.recsys`: Recommendation system.
- `articles`: Articles API.
- `comments`: Comments API.
- `followers`: Followers API.
- `reactions`: Reactions API.
- `tags`: Tags API.
- `users`: Users API.

## License

Licensed under MIT License

# Blog

[![Django CI](https://github.com/youzarsiph/blog/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/blog/actions/workflows/django.yml)
[![Black](https://github.com/youzarsiph/blog/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/blog/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/blog/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/blog/actions/workflows/ruff.yml)

Blog API built using Python, Django and DRF.

## Get started

Make sure you have Python installed on your machine, it is recommended to create a virtual env:

```bash
python -m venv .venv
source .venv/bin/activate
```

Clone the repo:

```bash
git clone https://github.com/youzarsiph/blog
```

If you have `make` on your system, you can use the `Makefile` to setup the project:

```bash
make setup
```

This command installs the dependencies, creates a project, configures the settings and runs migrations, checks and tests. You may need to configure `DRF` and `django-cors-headers` settings.

Install dependencies:

```bash
pip install -r blog/requirements.txt
```

Create a new project:

```bash
python -m django startproject mysite
mv -r blog mysite/blog
cd mysite
```

Use `blog`'s custom User model, in `mysite/settings.py`:

```python
AUTH_USER_MODEL = 'users.User'  # Add this line
```

Configure the settings, in `mysite/settings.py`:

```python
INSTALLED_APPS = [
    # Add the following lines
    "blog",
    "blog.ai",
    "blog.recsys",
    "blog.articles",
    "blog.comments",
    "blog.followers",
    "blog.reactions",
    "blog.reports",
    "blog.tags",
    "blog.users",
    "corsheaders",
    "drf_redesign",  # Makes the API interface prettier
    "rest_framework",  # REST Framework
    "rest_framework.authtoken",  # DRF Token authentication
    "django_filters",  # For filtering support
    "django_extensions",  # For running script that computes recommendations
]

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

```bash
python manage.py migrate
```

Run `makerecs` to compute recommendations:

```bash
python manage.py runscript makerecs
```

Create a `.env`file and add your [HuggingFace Token](https://huggingface.co), if you want to use the AI services:

```bash
HF_TOKEN=<YOUR_TOKEN>
```

Or you can export your token as an env variable:

```bash
export HF_TOKEN=<YOUR_TOKEN>
```

Replace `<YOUR_TOKEN>` with your actual HF token.

## Project Structure

The app consists of the following sub apps:

- `ai`: Provides extra actions for articles and comments like summarization, sentiment analysis etc...
- `articles`: Articles API.
- `comments`: Comments API.
- `followers`: Followers API.
- `reactions`: Reactions API.
- `recsys`: Recommendation system.
- `reports`: Abuse Reports API.
- `tags`: Tags API.
- `users`: Users API.

## License

Licensed under MIT License

format:
    python -m pip install --upgrade pip
    pip install black
    python -m black .

lint:
    python -m pip install --upgrade pip
    pip install ruff
    python -m ruff check *.py */**/.py

setup:
    # Install dependencies
    python -m pip install --upgrade pip
    pip install -r blog/requirements.txt

    # Create django project
    python -m django startproject mysite
    cp -r blog mysite/blog

    # Configure settings
    cd mysite
    echo "INSTALLED_APPS += ['blog', 'blog.ai', 'blog.articles', 'blog.comments', 'blog.followers', 'blog.reactions', 'blog.recsys', 'blog.reports', 'blog.tags', 'blog.users', 'rest_framework']" >> mysite/settings.py
    echo "AUTH_USER_MODEL = 'users.User'" >> mysite/settings.py
    echo "from django.urls import include" >> mysite/urls.py
    echo "urlpatterns += [path('', include('blog.urls'))]" >> mysite/urls.py

    # Run migrations, check and tests
    python manage.py migrate
    python manage.py check
    python manage.py test
    
# Generated by Django 5.0.2 on 2024-05-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, help_text="Article title", max_length=64
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Article Photo",
                        null=True,
                        upload_to="blog/images/articles/",
                    ),
                ),
                (
                    "content",
                    models.TextField(db_index=True, help_text="Article content"),
                ),
                (
                    "is_pinned",
                    models.BooleanField(
                        default=False, help_text="Designates if the Article is pinned"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Date published"),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        help_text="Article tags", related_name="articles", to="tags.tag"
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-16 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("text", models.TextField(db_index=True, help_text="Content")),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Date published"),
                ),
                (
                    "article",
                    models.ForeignKey(
                        help_text="Commented Article",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="articles.article",
                    ),
                ),
                (
                    "replies",
                    models.ManyToManyField(
                        help_text="Comment Replies", to="comments.comment"
                    ),
                ),
            ],
        ),
    ]
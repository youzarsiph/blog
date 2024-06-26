# Generated by Django 5.0.6 on 2024-06-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0006_article_recommendations"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="extras",
            field=models.JSONField(
                blank=True,
                help_text="Article extra data like summary etc...",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="headline",
            field=models.CharField(
                db_index=True, default="", help_text="Article headline", max_length=256
            ),
            preserve_default=False,
        ),
    ]

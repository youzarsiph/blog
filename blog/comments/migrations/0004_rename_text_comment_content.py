# Generated by Django 5.0.2 on 2024-05-21 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0003_alter_comment_article_alter_comment_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="text",
            new_name="content",
        ),
    ]
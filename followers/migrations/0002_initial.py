# Generated by Django 5.0.2 on 2024-05-16 07:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("followers", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="follower",
            name="from_user",
            field=models.OneToOneField(
                help_text="Follower",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="follower",
            name="to_user",
            field=models.OneToOneField(
                help_text="Followed",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddIndex(
            model_name="follower",
            index=models.Index(
                fields=["from_user", "to_user"], name="followers_f_from_us_83c873_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="follower",
            constraint=models.UniqueConstraint(
                fields=("from_user", "to_user"), name="unique_follower"
            ),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-08 21:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("goods", "0010_comment_level_comment_lft_comment_rght_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="added_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

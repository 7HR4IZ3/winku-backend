# Generated by Django 4.1.4 on 2023-11-20 19:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0009_alter_comment_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="followers",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="following",
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 11, 20, 19, 14, 59, 86953, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="profile",
            name="background_pic",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="display_pic",
            field=models.ImageField(default="default.png", upload_to="images"),
        ),
        migrations.CreateModel(
            name="Follow",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "follow_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follow_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

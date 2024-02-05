# Generated by Django 4.1.4 on 2023-10-05 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="city",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="country",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="display_pic",
            field=models.ImageField(
                blank=True, null=True, upload_to="frontend/assets/images"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="followers",
            field=models.ManyToManyField(
                blank=True, related_name="follower", to="main.profile"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="following",
            field=models.ManyToManyField(
                blank=True, related_name="follows", to="main.profile"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="posts",
            field=models.ManyToManyField(blank=True, to="main.post"),
        ),
    ]

# Generated by Django 4.1.4 on 2023-11-21 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_alter_follow_follow_user_alter_follow_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="main.profile"
            ),
        ),
        migrations.AlterField(
            model_name="follow",
            name="follow_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="follow_profile",
                to="main.profile",
            ),
        ),
        migrations.AlterField(
            model_name="follow",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="profile",
                to="main.profile",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="main.profile"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="viewers",
            field=models.ManyToManyField(
                blank=True, related_name="view", to="main.profile"
            ),
        ),
        migrations.AlterField(
            model_name="postreaction",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="main.profile"
            ),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-10 08:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "type",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=30)),
                ("message", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("telephone_prefix", models.IntegerField()),
                ("telephone_number", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Telephone",
            fields=[
                ("telephone_id", models.AutoField(primary_key=True, serialize=False)),
                ("phone", models.IntegerField()),
                ("prefix", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="VoteCategory",
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_numbers.category",
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_numbers.post",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="telephone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data_numbers.telephone"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("message", models.TextField()),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_numbers.post",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

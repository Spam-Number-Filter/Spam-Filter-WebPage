# Generated by Django 4.0.4 on 2022-05-12 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data_numbers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="category_name",
        ),
    ]
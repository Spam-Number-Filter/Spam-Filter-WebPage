# Generated by Django 4.0.3 on 2022-05-13 10:16

from django.db import migrations

categories = ["spam", "scam", "advertise"]


def create_types(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Category = apps.get_model("data_numbers", "Category")
    for category in categories:
        Category.objects.using(db_alias).create(type=category)


class Migration(migrations.Migration):
    dependencies = [
        ("data_numbers", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_types),
    ]

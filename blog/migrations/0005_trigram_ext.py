# Generated by Django 5.0.7 on 2024-07-13 09:05
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_tags"),
    ]

    operations = [
        TrigramExtension()
    ]

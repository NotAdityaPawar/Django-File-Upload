# Generated by Django 4.1 on 2022-08-18 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ner", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="file", name="date_added",),
    ]

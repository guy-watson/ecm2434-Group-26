# Generated by Django 5.0.dev20230124092027 on 2023-02-25 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("leaderboard", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="score",
            name="date",
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaderboard", "0003_score_privacy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score",
            name="privacy",
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0003_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("username", models.CharField(max_length=150, unique=True)),
                ("password", models.CharField(max_length=150)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
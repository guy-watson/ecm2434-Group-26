# Generated by Django 5.0.dev20230124092027 on 2023-03-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
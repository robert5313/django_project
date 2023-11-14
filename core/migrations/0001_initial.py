# Generated by Django 4.2.7 on 2023-11-14 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tutorial",
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
                ("name", models.CharField(max_length=50)),
                ("detail", models.CharField(max_length=225)),
                ("created_at", models.DateTimeField()),
            ],
        ),
    ]

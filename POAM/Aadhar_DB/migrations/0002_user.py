# Generated by Django 4.1.7 on 2023-02-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Aadhar_DB", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.BigIntegerField()),
                ("password", models.IntegerField()),
            ],
        ),
    ]

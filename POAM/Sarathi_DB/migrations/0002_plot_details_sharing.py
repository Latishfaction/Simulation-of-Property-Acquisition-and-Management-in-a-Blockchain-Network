# Generated by Django 4.1.7 on 2023-04-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Sarathi_DB", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plot_details",
            name="sharing",
            field=models.BooleanField(default=False),
        ),
    ]
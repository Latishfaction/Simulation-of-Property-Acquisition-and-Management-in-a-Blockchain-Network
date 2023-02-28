# Generated by Django 4.1.7 on 2023-02-28 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("LegalComplaints_DB", "0001_initial"),
        ("Sarathi_DB", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plot_details",
            name="is_blocked",
        ),
        migrations.CreateModel(
            name="blacklist",
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
                ("is_blocked", models.BooleanField(default=False)),
                (
                    "Property_case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="proprty_case",
                        to="LegalComplaints_DB.complaint",
                    ),
                ),
            ],
        ),
    ]

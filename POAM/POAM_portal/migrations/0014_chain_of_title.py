# Generated by Django 4.1.7 on 2023-04-18 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("POAM_portal", "0013_rename_people_person"),
    ]

    operations = [
        migrations.CreateModel(
            name="chain_of_title",
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
                ("ownership_date", models.DateField()),
                ("selling_date", models.DateField(blank=True, null=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner_title_chain",
                        to="POAM_portal.person",
                    ),
                ),
            ],
        ),
    ]

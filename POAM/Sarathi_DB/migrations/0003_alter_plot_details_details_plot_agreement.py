# Generated by Django 4.1.7 on 2023-04-18 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("POAM_portal", "0013_rename_people_person"),
        ("MuncipalCorporation_DB", "0007_chain_of_title"),
        ("Sarathi_DB", "0002_remove_plot_details_is_blocked_blacklist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plot_details",
            name="details",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="master_plot_details",
                to="MuncipalCorporation_DB.plot",
            ),
        ),
        migrations.CreateModel(
            name="plot_agreement",
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
                ("purchaser_sign", models.BooleanField(default=False)),
                ("buyer_sign", models.BooleanField(default=False)),
                ("total_amount", models.BigIntegerField()),
                ("agreement_duration", models.DateField()),
                ("purchaser_witness_sign", models.BooleanField(default=False)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="plot_buyer",
                        to="POAM_portal.person",
                    ),
                ),
                (
                    "buyer_witness",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="plot_buyer_witness",
                        to="POAM_portal.person",
                    ),
                ),
                (
                    "plot_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="plot_details",
                        to="MuncipalCorporation_DB.plot",
                    ),
                ),
                (
                    "purchaser",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="plot_purchaser",
                        to="POAM_portal.person",
                    ),
                ),
                (
                    "purchaser_witness",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="plot_purchaser_witness",
                        to="POAM_portal.person",
                    ),
                ),
            ],
        ),
    ]

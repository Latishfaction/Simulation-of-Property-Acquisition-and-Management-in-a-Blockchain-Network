# Generated by Django 4.1.7 on 2023-02-28 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("POAM_portal", "0001_initial"),
        (
            "MuncipalCorporation_DB",
            "0003_alter_plot_area_alter_plot_length_alter_plot_width",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="plot",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plot_owner",
                to="POAM_portal.person",
            ),
        ),
    ]

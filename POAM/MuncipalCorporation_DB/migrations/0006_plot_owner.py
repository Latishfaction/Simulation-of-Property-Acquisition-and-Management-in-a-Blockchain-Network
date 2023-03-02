# Generated by Django 4.1.7 on 2023-03-02 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("POAM_portal", "0013_rename_people_person"),
        ("MuncipalCorporation_DB", "0005_remove_plot_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="plot",
            name="owner",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plot_owner",
                to="POAM_portal.person",
            ),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-01 16:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("MuncipalCorporation_DB", "0005_remove_plot_owner"),
        ("Bank_DB", "0002_remove_account_acc_holder_name_and_more"),
        ("POAM_portal", "0010_alter_person_date_joined"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Person",
        ),
    ]
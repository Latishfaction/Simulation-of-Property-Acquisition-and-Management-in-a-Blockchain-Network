# Generated by Django 4.1.7 on 2023-02-28 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "Aadhar_DB",
            "0005_person_date_joined_person_email_person_first_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="date_joined",
            field=models.DateField(
                default=datetime.datetime(2023, 3, 1, 0, 1, 28, 883863)
            ),
        ),
    ]

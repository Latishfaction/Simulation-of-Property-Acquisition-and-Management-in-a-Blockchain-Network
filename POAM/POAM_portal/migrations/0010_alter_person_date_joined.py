# Generated by Django 4.1.7 on 2023-03-01 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("POAM_portal", "0009_alter_person_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="date_joined",
            field=models.DateField(
                default=datetime.datetime(2023, 3, 1, 22, 21, 37, 42933)
            ),
        ),
    ]

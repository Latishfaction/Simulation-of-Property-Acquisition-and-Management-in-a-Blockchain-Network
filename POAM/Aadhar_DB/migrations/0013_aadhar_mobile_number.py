# Generated by Django 4.1.7 on 2023-04-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Aadhar_DB", "0012_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="aadhar",
            name="mobile_number",
            field=models.CharField(max_length=10, null=True),
        ),
    ]

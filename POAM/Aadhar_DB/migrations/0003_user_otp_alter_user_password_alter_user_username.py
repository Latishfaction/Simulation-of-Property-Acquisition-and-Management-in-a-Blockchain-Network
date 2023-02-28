# Generated by Django 4.1.7 on 2023-02-28 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Aadhar_DB", "0002_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="otp",
            field=models.IntegerField(default=1111),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(default="1111", max_length=30),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to="Aadhar_DB.aadhar",
            ),
        ),
    ]

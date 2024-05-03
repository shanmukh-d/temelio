# Generated by Django 4.2.11 on 2024-05-02 23:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nonprofits", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="nonprofit",
            name="address",
        ),
        migrations.AlterField(
            model_name="nonprofit",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

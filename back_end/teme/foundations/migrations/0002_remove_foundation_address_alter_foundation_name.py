# Generated by Django 4.2.11 on 2024-05-03 01:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("foundations", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="foundation",
            name="address",
        ),
        migrations.AlterField(
            model_name="foundation",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
# Generated by Django 4.2.11 on 2024-05-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nonprofits", "0003_nonprofit_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sentemails",
            name="sent_from",
            field=models.EmailField(db_index=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="sentemails",
            name="sent_to",
            field=models.EmailField(db_index=True, max_length=254),
        ),
    ]

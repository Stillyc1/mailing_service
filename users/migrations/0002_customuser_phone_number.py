# Generated by Django 5.1.3 on 2024-12-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermail",
            name="email",
            field=models.EmailField(max_length=150, unique=True, verbose_name="Email"),
        ),
    ]

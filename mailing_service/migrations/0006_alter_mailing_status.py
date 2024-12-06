# Generated by Django 5.1.3 on 2024-12-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "mailing_service",
            "0005_alter_mailing_options_alter_mailingattempt_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("Создана", "Создана"),
                    ("Запущена", "Запущена"),
                    ("Завершена", "Завершена"),
                    ("Отключена", "Отключена"),
                ],
                default="Создана",
                max_length=9,
                verbose_name="Статус",
            ),
        ),
    ]